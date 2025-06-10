# Veille Technologique Proactive – Projet fastIA

## Introduction
Bienvenue dans le projet de veille technologique proactive pour l'équipe fastIA. Ce projet vise à automatiser la collecte, l'analyse et la restitution d'informations sur l'éthique, la gouvernance des données et la vie privée en intelligence artificielle.

---

## Sommaire
- [Objectifs](#objectifs)
- [Installation](#installation)
- [Collecte automatisée avec n8n](#collecte-automatisée-avec-n8n)
- [Analyse et résumé avec Python](#analyse-et-résumé-avec-python)
- [Restitution](#restitution)
- [Outils recommandés](#outils-recommandés)
- [Ressources](#ressources)

---

## Objectifs
- **Automatiser la veille** via des flows n8n (arXiv, RSS, etc.)
- **Analyser et résumer** les articles collectés avec Python
- **Restituer** la veille sous forme de rapport Markdown structuré

---

## Installation
### Prérequis
- Node.js ≥ 18
- npm
- Python ≥ 3.8

### Étapes
1. **Cloner le projet**
2. **Créer un environnement virtuel Python**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Installer les dépendances Python**
   ```bash
   pip install -r requirements.txt
   ```
4. **Installer n8n**
   ```powershell
   npm install -g n8n
   ```
5. **Lancer n8n**
   ```powershell
   n8n
   ```

---

## Collecte automatisée avec n8n
- Le flow principal (`workflows/collect_arxiv_ethique.json`) interroge arXiv sur l'éthique et l'IA, puis enregistre les résultats dans `files/arxiv_ethique_ia.json`.
- Vous pouvez adapter ou ajouter d'autres flows pour d'autres sources (RSS, Google Alerts, etc.).

---

## Analyse et résumé avec Python
- Le script `analyse.py` lit le fichier JSON généré par n8n, extrait les articles, effectue un scraping de l'abstract et génère un résumé automatique avec un modèle NLP.
- Dépendances nécessaires : `requests`, `beautifulsoup4`, `transformers`, `torch`.
- Exemple d'exécution :
  ```bash
  python analyse.py > rapport_veille.md
  ```

---

## Restitution
- Le rapport généré (`rapport_veille.md`) respecte la structure Markdown demandée (titres, listes, liens, styles, etc.).
- À intégrer dans la documentation finale à remettre au client.

---

## Outils recommandés
- [n8n](https://n8n.io/) : automatisation de la collecte
- [Feedly](https://feedly.com/), [Inoreader](https://www.inoreader.com/), [Pocket](https://getpocket.com/)
- [arXiv](https://arxiv.org/), [Semantic Scholar](https://www.semanticscholar.org/)
- [Notion](https://www.notion.so/), [Evernote](https://evernote.com/)

---

## Ressources
- [Documentation n8n](https://docs.n8n.io/hosting/installation/)
- [Guide Feedly](https://blog.feedly.com/getting-started/)
- [RGPD et IA (CNIL)](https://www.cnil.fr/fr/intelligence-artificielle)

---

*Projet réalisé dans le cadre d'une demande client Impact France – fastIA*
