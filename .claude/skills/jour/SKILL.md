---
name: jour
description: Mène une journée de l'Intensive AI Engineering Class d'Akram (rappel espacé, théorie socratique, cahier, pratique, trace) et produit la page publique du jour. Utiliser quand il dit « /jour », « jour 12 », « on fait la journée » ou « on continue la classe ».
argument-hint: "[numéro du jour]"
---

# Mener une journée de la classe

Jour demandé : $ARGUMENTS. Sans numéro, prends le prochain jour de `contexte/suivi.md`.

Une journée dure environ 1 h et suit toujours la même recette, dans le même ordre : Akram aime les recettes fixes. Un seul moment par réponse ; pendant la théorie, une seule question par message.

## Avant la séance
1. Lis la fiche du jour dans `contexte/programme.md`, puis `contexte/suivi.md` (carte des niveaux, révisions dues), puis l'entrée la plus récente de `contexte/journal.md`.
2. Lis la fiche du même jour N dans la classe jumelle (`../Intensive Inference Engineering Class/contexte/programme.md`), cette section seulement. Si un concept se recoupe, prévois un renvoi d'une phrase vers l'autre classe ; ne refais pas sa théorie.
3. Le jour ouvre une phase pas encore détaillée ? Détaille-la d'abord dans `programme.md` : une fiche par jour, chaque source vérifiée (lien, durée, passage précis en minutes ou en section). Écris aussi le guide du projet de la phase dans `contexte/guides/`, sur le modèle de `../parcours-ia/contexte/guides/P1-boosting-validation.md`.
4. Prépare la page : copie `gabarits/jour.html` vers `docs/jours/jour-NNN/index.html` (NNN sur trois chiffres), puis remplis les `{{...}}`. Garde le repère « À ÉCRIRE PAR AKRAM » : la vérification bloque la publication tant qu'il reste. La démo montre une seule idée, se comprend en 10 secondes et prend un exemple de transport ; une valeur simulée est étiquetée comme telle. Vérifie le rendu avec `python outils/capturer_page.py docs/jours/jour-NNN/index.html`, puis lis les deux images.

## La recette
### 1. Rappel (5 min)
Pose une ou deux révisions dues dans `suivi.md`, une question à la fois, sans dire de quel jour elle vient. Une révision ratée fait baisser le niveau d'un cran et ramène la sous-compétence plus tôt.

À l'ouverture d'une phase, le rappel devient le diagnostic du protocole socratic-tutor : 3 à 5 questions, de la plus facile à la plus difficile, une à la fois, sans rien enseigner avant la fin. Montre ensuite la carte de la phase.

### 2. Théorie (20 min)
Suis le protocole de `.claude/skills/socratic-tutor/SKILL.md` : une question par message ; lui faire prédire, expliquer, trouver la faille d'une affirmation ; évaluation stricte. Avec ces adaptations :
- **Ce qui ne se devine pas s'enseigne d'abord.** Une définition, une convention ou un mécanisme nouveau (par exemple requête, clé et valeur) passe par la page du jour : schéma, mini-exemple chiffré, pseudo-code. Les questions viennent ensuite, pour vérifier et faire raisonner, jamais pour lui faire deviner une définition.
- Donne ensuite le passage précis de la source et dis en une phrase ce qu'il doit y chercher.
- Après deux essais ratés : une explication courte et visuelle, puis un nouveau test sous un autre angle.
- « Dis-le-moi » : réponds à cette question seulement, puis reprends le questionnement.
- Pars de ce qu'il connaît : trafic, BIXI, graphes, forêts aléatoires.
- Le bloc « save state » du protocole est remplacé par `contexte/suivi.md`.

### 3. Cahier (10 min)
Il note à la main, dans son cahier papier, l'idée en une phrase, le schéma, le mini-exemple et le pseudo-code. Le cahier reste privé.

### 4. Pratique (20 min)
Il crée son carnet `docs/jours/jour-NNN/jour-NNN.ipynb`, avec le noyau Jupyter « parcours-ia » (le `.venv` du cerveau : PyTorch, pandas, scikit-learn). Les règles de `/projet` s'appliquent :
- Le code arrive morceau par morceau, avec son pseudo-code, « Prédis » avant de lancer et « Tu devrais voir » après.
- La figure passe par `style/charte.py` (`sys.path.insert(0, "../../../style")`) et s'enregistre dans le dossier du jour en `_clair.png` et `_sombre.png`.
- Les données éventuelles vont dans `docs/jours/jour-NNN/donnees/`, que git ignore.

Il écrit ensuite « Ce que j'ai fait, en mes mots » : trois ou quatre phrases, ce qu'il a fait et compris, ce qui l'a surpris. Place-les dans `#mots`, à la place du repère, avec sa figure dans une balise `<picture>` et le lien vers son carnet sur GitHub. Tu peux corriger la langue, jamais les idées.

### 5. Trace (5 min)
1. Mets à jour `contexte/suivi.md` :
   - les niveaux, seulement sur preuve : 2 vérifications indépendantes, dont un rappel sans aide ;
   - les révisions dues à J+1, J+3, J+7 et J+21, comptées en jours du programme ;
   - la ligne du jour, avec sa date privée et sa durée.
2. Ajoute le jour au bloc JSON `jours-publies` de `docs/index.html`, puis mets à jour le compteur N/140 du README.
3. Les gestes de publication sont à lui (voir `/publier`) :
   - il lance `python -m pytest` et `python outils/verifier_avant_publication.py` ;
   - il ajoute les fichiers du jour nommément et relit `git diff --cached` avec toi ;
   - il commit sans ligne de co-auteur, puis pousse. Vérifie ensuite la page en ligne.
4. Ajoute une entrée dans `contexte/journal.md` : ce qu'il a compris, ce qui a bloqué, ce que tu as fait à sa place.

## Jours de projet
Il y en a un tous les 7 à 10 jours (voir `programme.md`). Suis `/projet` avec le guide de la phase, `/coach` pour la pièce sans aide, et `/quiz` en fin de phase. Le projet vit dans le dossier de son jour (`docs/jours/jour-NNN/`). P4, repris en phase 3, garde son code, son guide et son corrigé dans le cerveau (`../parcours-ia/`).

## Public contre privé
- **Public** : la page du jour (notions et démo signées « l'assistant IA », ses mots, sa trace), son carnet et ses figures. Les pages disent « Jour N », jamais une date.
- **Privé** : les niveaux, les révisions, les erreurs, les indices, les prédictions ratées et le cahier.
