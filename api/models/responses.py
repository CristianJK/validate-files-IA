from pydantic import BaseModel, Field

class HeuristicScore(BaseModel):
    filler_phrases: dict
    triple_list: dict
    sentence_uniformity: dict
    repeated_structures: dict
    dash_usage: dict
    formulaic_vocabulary: dict

class StatisticalScore(BaseModel):
    perplexity: dict
    lexical_entropy: dict
    type_token_ratio: dict
    repeated_ngrams: dict

class MetadataScore(BaseModel):
    score: float
    author: Optional[str] = None
    revision: Optional[str] = None
    details: list[dict]

class AnalysysResponse(BaseModel):
    success: bool
    filename: Optional[str]
    final_score: float
    label: str
    risk_level: str
    summary: dict
    heuristic_score: HeuristicScore
    statistical_score: StatisticalScore
    metadata_score: MetadataScore
    scoring_weights: dict

class CorrectionDetail(BaseModel):
    paragraph_index: int
    original:str
    corrected:str
    changes: list[dict]

class CorrectionResponse(BaseModel):
    success: bool
    filename: Optional[str]
    corrections_applied: int
    correction_details: list[CorrectionDetail]
    score_before: float
    score_after: float
    score_reduction: float

class HealthResponse(BaseModel):
    success: str
    model_loaded: bool
    model_name: str
    spacy_models: list[str]
    uptime_seconds: float