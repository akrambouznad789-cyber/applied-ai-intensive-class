---
name: publier
description: Vérifie le contenu public de la classe et prépare le push avec Akram, qui tape lui-même les commandes. Utiliser quand il dit « /publier », « mets ça en ligne » ou « envoie sur GitHub ».
disable-model-invocation: true
---

# Publier sur GitHub

Le site de la classe fait partie de son portfolio public : une erreur ici se voit par des recruteurs et reste dans l'historique de git. C'est lui qui tape `git add`, `git commit` et `git push` ; `.claude/settings.json` t'interdit le push.

1. Il lance `python -m pytest`, puis `python outils/verifier_avant_publication.py`. Au moindre problème, arrêtez-vous et corrigez.
2. Vérifie le rendu des pages modifiées avec `python outils/capturer_page.py`, puis lis les images.
3. Il ajoute les fichiers nommément ; relisez ensemble `git diff --cached`. Cherche ce qu'un script ne voit pas : une affirmation exagérée, un résultat sans preuve, un titre d'ingénieur, un élément de sa recherche d'emploi, un fichier de données suivi.
4. Il écrit son message de commit, sans ligne de co-auteur, puis fait `git push`. Vérifie ensuite la page en ligne.

## Première publication
`gh` n'est pas installé. Le nom du dépôt est dans `CLAUDE.md` ; l'adresse de commit anonyme est déjà réglée dans ce dépôt (`git config --local user.email`).
1. Akram crée le dépôt public sur github.com, sans README ni licence.
2. `git remote add origin https://github.com/akrambouznad789-cyber/<nom-du-dépôt>.git`, puis le premier `git push -u origin main`.
3. Sur github.com : Settings, Pages, branche `main`, dossier `/docs`.
4. Le site sera à `https://akrambouznad789-cyber.github.io/<nom-du-dépôt>/`. La page d'accueil du parcours (dépôt `roadmap-ia`) y renvoie déjà.
