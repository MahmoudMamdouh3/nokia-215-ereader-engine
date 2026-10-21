from soundlab.ingestion import IngestionEngine

url = "https://www.youtube.com/watch?v=_8oKD8I6hRQ"
print(f"Ingesting Kobe Basketball Academy 2012 Q&A: {url}...")
engine = IngestionEngine()
res = engine.download_url(url)
print(f"Result: {res}")
