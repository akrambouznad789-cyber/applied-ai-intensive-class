# Intensive AI Engineering Class

Une classe intensive de 140 jours en IA appliquée : des données jusqu'à un modèle de langage ouvert mis en service en local. La théorie d'abord, une page par jour, un projet de consolidation tous les 7 à 10 jours.

**Site : https://akrambouznad789-cyber.github.io/intensive-ai-engineering-class/**

**Progression : 1 jour publié sur 140.**

Classe sœur : l'[Intensive Inference Engineering Class](https://github.com/akrambouznad789-cyber/intensive-inference-engineering-class), menée en parallèle, au même numéro de jour. Les deux classes partent de la [page d'accueil du parcours](https://akrambouznad789-cyber.github.io/roadmap-ia/).

## Une journée

Une séance d'environ une heure par jour, toujours dans le même ordre :

1. **Notions** : la théorie d'abord, par un schéma, un mini-exemple chiffré et un pseudo-code, puis un passage précis d'une source de référence.
2. **Démo** : une page interactive qui montre l'idée sur un cas de transport.
3. **Pratique, en ses mots** : un carnet qui refait le calcul et produit une figure, puis ce qui a été fait et compris, en quelques phrases.

## La route

| Phase | Jours | Contenu | État |
|---|---|---|---|
| 1 · Apprendre à partir de données | 1 à 8 | perte et descente de gradient, entropie croisée, arbres et boosting, surapprentissage, validation sans fuite, K-moyennes et ACP | En cours |
| 2 · Réseaux de neurones et PyTorch | 9 à 26 | rétropropagation, optimiseurs, tenseurs, entraînement, régularisation, plongements, convolution, graphes | À venir |
| 3 · Langage et Transformer | 27 à 50 | tokenisation BPE, attention, bloc Transformer, entraînement et échantillonnage d'un petit GPT | À venir |
| 4 · Se servir d'un LLM ouvert en local | 51 à 64 | exécution locale, consignes, sorties structurées, appels d'outils | À venir |
| 5 · Évaluation | 65 à 78 | jeux de test, LLM juge, lecture des échecs, tests A/B et causalité | À venir |
| 6 · RAG | 79 à 92 | découpage, index vectoriel, recherche hybride, réponse ancrée | À venir |
| 7 · Agents | 93 à 112 | boucle d'agent, outils, mémoire, garde-fous, évaluation de trajectoires | À venir |
| 8 · Affinage | 113 à 126 | données d'affinage, SFT, LoRA et QLoRA, préférences, entraînement réparti et diffusion en miniature | À venir |
| 9 · Mise en service et bilan | 127 à 140 | API locale, surveillance, sécurité, projet final | À venir |

## Contenu du dépôt

| Dossier | Contenu |
|---|---|
| `docs/` | Le site : la route des 140 jours, puis une page, un carnet et des figures par jour (`docs/jours/`) |
| `gabarits/` | Le modèle d'une page de jour |
| `style/` | La charte des figures |
| `outils/`, `tests/` | La vérification des pages avant publication et la capture de leur rendu, avec leurs tests |

## Données

Les données brutes ne sont pas versionnées, seulement les petits résultats. Chaque source est créditée sur la page de son jour.

Mise en page et démos : l'assistant IA. Carnets, figures et mots : Akram.
