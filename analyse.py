import json
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

def scrap_and_summarize(url):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # Récupère le texte principal (simplifié pour arXiv)
        abstract = ''
        if 'arxiv.org' in url:
            abs_div = soup.find('blockquote', class_='abstract')
            if abs_div:
                abstract = abs_div.text.replace('Abstract:', '').strip()
        if not abstract:
            # fallback: tout le texte de la page
            abstract = soup.get_text()[:2000]
        # Résumé automatique (limite à 1024 tokens)
        summary = summarizer(abstract, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"Erreur scraping/résumé: {e}"

with open('files/arxiv_ethique_ia.json', encoding='utf-8') as f:
    data = json.load(f)
articles = json.loads(data['data'])

print('# Résultats de la veille sur l\'éthique en IA\n')
for art in articles:
    print(f"- **{art['title']}** ({art['published']})  ")
    print(f"  {art['link']}")
    resume = scrap_and_summarize(art['link'])
    print(f"  _Résumé_: {resume}\n")