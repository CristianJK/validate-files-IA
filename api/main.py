from fastapi import FastAPI

app = FastAPI(title="Detector de IA y generador de documento con leguaje natural")

@app.get("/api/health")
def health():
    return { "status" : "ok"}