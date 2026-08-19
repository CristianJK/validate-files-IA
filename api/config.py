from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    scoring_weights : dict = {
        "perplexity": 0.40,
        "heuristic": 0.25,
        "uniformity": 0.20,
        "metadata": 0.15
    }

    model_name : str = "gpt-4o-mini"
    spacy_models : list[str] = ["en_core_web_sm", "es_core_news_sm"]
    max_file_size : int = 10 * 1024 * 1024  # 10 MB
    allowed_file_types : list[str] = [".txt", ".pdf", ".docx"]
    upload_dir: str = "./uploads"
settings = Settings()