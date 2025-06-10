import requests
import json
import os
from datetime import datetime
from loguru import logger
from fastapi import FastAPI, HTTPException, Request, Query
from pydantic import BaseModel
import os
from myapp_base import setup_loguru, create_app

logger = setup_loguru("logs/collect_scholar.log")
app = create_app()


class Texte(BaseModel):
    texte: str

# Standard de retour pour un article
class Article(BaseModel):
    title: str
    url: str
    authors: str
    published_date: str
    source: str
    search_date: str
    keywords: str
    abstract: str = ""

@app.get("/")
async def root(request: Request):
    logger.info(f"Route '{request.url.path}' called by  {request.client.host}")
    return {"message": "Bienvenue sur l'API"}




# Recherche sur Semantic Scholar (français, éthique et IA)
query = "les biais éthiques"

# url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=10&fields=title,authors,year,url,abstract,language,publicationDate"
# resp = requests.get(url)
# data = resp.json()

# logger.info(f"Q semanticscholar '{data}'")

# # Filtrer les articles en français
# results = [paper for paper in data.get('data', []) if paper.get('language', '').startswith('fr')]

# # Charger les articles existants s'ils existent
# filepath = 'files/scholar_ethique_ia.json'
# if os.path.exists(filepath):
#     with open(filepath, encoding='utf-8') as f:
#         existing = json.load(f)
# else:
#     existing = []

# # Index des articles existants par URL pour éviter les doublons
# existing_urls = {art['url'] for art in existing if 'url' in art}

# # Ajouter la date de recherche et les mots-clés
# date_recherche = datetime.now().strftime('%Y-%m-%d %H:%M')
# for art in results:
#     art['date_recherche'] = date_recherche
#     art['mots_cles'] = query

# # Ajouter uniquement les nouveaux articles
# new_articles = [art for art in results if art.get('url') not in existing_urls]
# all_articles = existing + new_articles

# # Trier par date de publication décroissante (si disponible)
# def get_pubdate(art):
#     return art.get('publicationDate') or art.get('year') or ''
# all_articles.sort(key=get_pubdate, reverse=True)

# # Sauvegarder
# with open(filepath, 'w', encoding='utf-8') as f:
#     json.dump(all_articles, f, ensure_ascii=False, indent=2)

# print(f"{len(new_articles)} nouveaux articles ajoutés. Total: {len(all_articles)} dans files/scholar_ethique_ia.json")

# Route pour OpenAlex
@app.get("/openalex")
async def get_openalex(request: Request, q: str = Query(..., description="Mots-clés de recherche"), log: bool = False, ):
    url = f"https://api.openalex.org/works?filter=title.search:{q}&per-page=10"
    resp = requests.get(url)
    data = resp.json()
    logger.info(f"Route '{request.url.path}' url : {url}")
    search_date = datetime.now().strftime('%Y-%m-%d %H:%M')
    articles = []
    for work in data.get('results', []):
        # Correction: certains champs peuvent être absents ou None
        authors = ', '.join([a['author'].get('display_name', '') for a in work.get('authorships', []) if a.get('author')])
        # Abstract peut être un dict (inverted index) ou absent
        abstract = ''
        if isinstance(work.get('abstract_inverted_index'), dict):
            # Reconstruire l'abstract à partir de l'inverted index
            idx = work['abstract_inverted_index']
            words = [None] * (max([max(v) for v in idx.values()]) + 1) if idx else []
            for word, positions in idx.items():
                for pos in positions:
                    words[pos] = word
            abstract = ' '.join([w for w in words if w])
        elif isinstance(work.get('abstract_inverted_index'), str):
            abstract = work['abstract_inverted_index']
        articles.append(Article(
            title=work.get('display_name', ''),
            url=work.get('id', ''),
            authors=authors,
            published_date=work.get('publication_date', work.get('publication_year', '')),
            source="openalex",
            search_date=search_date,
            keywords=q,
            abstract=abstract
        ).dict())
    if log and articles:
        filepath = 'files/scholar_ethique_ia.json'
        if os.path.exists(filepath):
            with open(filepath, encoding='utf-8') as f:
                existing = json.load(f)
        else:
            existing = []
        # Index existants pour éviter les doublons
        existing_urls = {art['url'] for art in existing if 'url' in art}
        new_articles = [art for art in articles if art['url'] not in existing_urls]
        all_articles = existing + new_articles
        # Tri décroissant par date
        def get_pubdate(art):
            return art.get('published_date') or ''
        all_articles.sort(key=get_pubdate, reverse=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(all_articles, f, ensure_ascii=False, indent=2)
        logger.info(f"{len(new_articles)} new articles from openalex logged. Total: {len(all_articles)}.")
    return {"results": articles}
