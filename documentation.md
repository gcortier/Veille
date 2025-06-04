- Documentation for n8n
https://workos.com/blog/n8n-the-workflow-automation-tool-for-the-ai-age

## Installation de n8n (version open source, auto-hébergée)

### Prérequis
- Node.js (version 18 ou supérieure recommandée)
- npm (installé avec Node.js)

### Étapes d'installation sous Windows

1. **Ouvrir PowerShell**
2. Installer n8n globalement :
```powershell
npm install -g n8n
```
3. Lancer n8n :
```powershell
n8n
```
4. Accéder à l’interface web :
- Ouvrir votre navigateur sur [http://localhost:5678](http://localhost:5678)

### Documentation officielle
- [Guide d'installation n8n](https://docs.n8n.io/hosting/installation/)

### Conseils
- Pour un usage avancé (persistant, multi-utilisateur, production), privilégier l’installation via Docker ou sur un serveur dédié.
- Pour arrêter n8n, utiliser `Ctrl+C` dans le terminal.

---


### Qui est Impact France ?

**Impact France** est un mouvement français rassemblant des entreprises et entrepreneurs engagés pour une économie à impact social et écologique positif. Leur mission est de promouvoir une gouvernance responsable, l'inclusion, et la transition écologique dans le monde économique. *Impact France* agit comme un réseau d'influence, propose des plaidoyers et accompagne les organisations vers des pratiques plus durables.

[En savoir plus sur Impact France](https://www.impactfrance.eco/plaidoyer)



### Test flow simple n8n : 
- Je rentre un texte dans le chat et ça rempli une feuille sheet Google Sheets
- sheet : https://docs.google.com/spreadsheets/d/11nA-isgpEki3fr40gdcJ3K2gvLwlTAu8UrbLrEo4xqU/edit?gid=0#gid=0


### Installation Ollama
https://ollama.com/download


### 
pip install requests beautifulsoup4 transformers torch