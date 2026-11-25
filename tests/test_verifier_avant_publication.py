import subprocess

import pytest

from verifier_avant_publication import lire_mots_interdits, verifier_depot

# Assemblés ici pour que ce fichier public ne déclenche pas lui-même la vérification.
FAUX_TELEPHONE = "514" + "-555-" + "0199"
FAUX_CHEMIN_LOCAL = "C:" + "\\Users\\quelquun\\fichier.txt"
REPERE_FRANCAIS = "À ÉCRIRE " + "PAR AKRAM"
REPERE_ANGLAIS = "TO BE WRITTEN " + "BY AKRAM"

PAGE_JOUR_VALIDE = """<!doctype html>
<html lang="fr"><head><title>Jour 1</title></head><body>
<section id="notions"></section><section id="demo"></section>
<section id="mots">Mes mots.</section><section id="sources"></section>
</body></html>"""

PAGE_DAY_VALIDE = PAGE_JOUR_VALIDE.replace('lang="fr"', 'lang="en"').replace("Jour 1", "Day 1")


def carnet_avec_sortie(texte_de_sortie):
    """Un carnet Jupyter minimal (JSON) dont l'unique cellule affiche `texte_de_sortie`."""
    sortie_echappee = texte_de_sortie.replace("\\", "\\\\")
    return (
        '{"cells": [{"cell_type": "code", "source": ["print(1)"], "outputs": '
        '[{"output_type": "stream", "name": "stdout", "text": ["' + sortie_echappee + '\\n"]}]}], '
        '"metadata": {}, "nbformat": 4, "nbformat_minor": 5}'
    )


@pytest.fixture
def depot(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".gitignore").write_text("contexte/\n", encoding="utf-8")
    return tmp_path


def ecrire(depot, chemin_relatif, contenu):
    chemin = depot / chemin_relatif
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(contenu, encoding="utf-8")


def test_une_page_de_jour_complete_passe(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE)
    assert verifier_depot(depot, []) == []


def test_une_page_anglaise_complete_passe(depot):
    ecrire(depot, "docs/days/day-001/index.html", PAGE_DAY_VALIDE)
    assert verifier_depot(depot, []) == []


def test_detecte_un_numero_de_telephone(depot):
    ecrire(depot, "README.md", f"Appelle-moi au {FAUX_TELEPHONE}")
    assert any("numéro de téléphone" in probleme for probleme in verifier_depot(depot, []))


def test_les_dates_ne_passent_pas_pour_un_telephone(depot):
    ecrire(depot, "resultats.csv", "2026-10-31,llama3.2:3b,1,128,5.25\n")
    assert verifier_depot(depot, []) == []


def test_detecte_un_chemin_local(depot):
    ecrire(depot, "README.md", FAUX_CHEMIN_LOCAL)
    assert any("chemin local" in probleme for probleme in verifier_depot(depot, []))


def test_detecte_un_mot_prive_sans_tenir_compte_de_la_casse(depot):
    ecrire(depot, "docs/note.md", "Mon employeur SECRET")
    assert any("mot privé" in probleme for probleme in verifier_depot(depot, ["secret"]))


def test_ignore_ce_que_git_ne_publierait_pas(depot):
    ecrire(depot, "contexte/notes.md", f"Tel : {FAUX_TELEPHONE}, employeur secret")
    assert verifier_depot(depot, ["secret"]) == []


def test_refuse_les_poids_de_modele(depot):
    ecrire(depot, "modeles/llama.gguf", "contenu")
    assert any("type de fichier interdit" in probleme for probleme in verifier_depot(depot, []))


def test_bloque_une_page_avec_le_repere_francais(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE.replace("Mes mots.", REPERE_FRANCAIS))
    assert any("texte à écrire" in probleme for probleme in verifier_depot(depot, []))


def test_bloque_une_page_avec_le_repere_anglais(depot):
    ecrire(depot, "docs/days/day-001/index.html", PAGE_DAY_VALIDE.replace("Mes mots.", REPERE_ANGLAIS))
    assert any("texte à écrire" in probleme for probleme in verifier_depot(depot, []))


def test_bloque_un_gabarit_non_rempli(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE.replace("Mes mots.", "{{TITRE}}"))
    assert any("gabarit non rempli" in probleme for probleme in verifier_depot(depot, []))


def test_exige_toutes_les_sections_d_une_page_de_jour(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE.replace('id="notions"', 'id="autre"'))
    assert any("section #notions manquante" in probleme for probleme in verifier_depot(depot, []))


def test_exige_toutes_les_sections_d_une_page_anglaise(depot):
    ecrire(depot, "docs/days/day-001/index.html", PAGE_DAY_VALIDE.replace('id="mots"', 'id="autre"'))
    assert any("section #mots manquante" in probleme for probleme in verifier_depot(depot, []))


def test_la_page_de_la_route_n_exige_pas_de_sections(depot):
    ecrire(depot, "docs/index.html", '<html lang="fr"><title>140 jours</title></html>')
    assert verifier_depot(depot, []) == []


def test_detecte_un_chemin_local_dans_la_sortie_d_un_carnet(depot):
    ecrire(depot, "docs/jours/jour-001/jour-001.ipynb", carnet_avec_sortie(FAUX_CHEMIN_LOCAL))
    assert any("chemin local" in probleme for probleme in verifier_depot(depot, []))


def test_un_carnet_avec_des_grands_nombres_passe(depot):
    # Les grands nombres à la française (espaces) ne doivent pas passer pour un téléphone.
    ecrire(depot, "docs/jours/jour-001/jour-001.ipynb", carnet_avec_sortie("13 605 052 trajets, 2 219 474 en juillet"))
    assert verifier_depot(depot, []) == []


def test_detecte_un_lien_brise(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE.replace("</body>", '<a href="absent.html">x</a></body>'))
    assert any("lien brisé" in probleme for probleme in verifier_depot(depot, []))


def test_accepte_un_lien_vers_un_dossier_avec_index(depot):
    ecrire(depot, "docs/jours/jour-001/index.html", PAGE_JOUR_VALIDE)
    ecrire(depot, "docs/index.html", '<html lang="fr"><title>Route</title><a href="jours/jour-001/">x</a></html>')
    assert verifier_depot(depot, []) == []


def test_les_liens_externes_ne_sont_pas_verifies(depot):
    ecrire(depot, "docs/index.html", '<html lang="fr"><title>A</title><a href="https://exemple.org/absent">x</a></html>')
    assert verifier_depot(depot, []) == []


def test_une_liste_absente_est_une_erreur_en_local(tmp_path, monkeypatch):
    monkeypatch.delenv("CI", raising=False)
    with pytest.raises(FileNotFoundError):
        lire_mots_interdits(tmp_path / "absent.txt")


def test_une_liste_absente_est_toleree_sur_github_actions(tmp_path, monkeypatch):
    monkeypatch.setenv("CI", "true")
    assert lire_mots_interdits(tmp_path / "absent.txt") is None


def test_la_liste_ignore_les_commentaires_et_les_lignes_vides(tmp_path):
    chemin = tmp_path / "mots.txt"
    chemin.write_text("# commentaire\n\nmot un\n  mot deux  \n", encoding="utf-8")
    assert lire_mots_interdits(chemin) == ["mot un", "mot deux"]
