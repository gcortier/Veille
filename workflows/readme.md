# Installation
## Génération de l'environnement virtuel en début de projet
`python -m venv .venv`

## Activation de l'environnement virtuel
- Windows :  `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`


## Installer n8n globalement :
```powershell
npm install -g n8n
npm install fast-xml-parser
```
## Lancer n8n :
```powershell
n8n
```


## installation des bibliothèques de base
- ### installation modules pour n8n
- `pip install fast-xml-parser`


### Génération requirements.txt à chaque installation de module
- `pip freeze > requirements.txt`

### ou directement : 
- `pip install -r requierements.txt`


## run server uvicorn :
- `uvicorn collect_scholar:app --host 127.0.0.1 --port 9000 --reload`

## lancer le client streamlit:
`streamlit run app.py`