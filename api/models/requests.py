from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=50000)
    lang: str = Field"es", pattern="^(en|es)$")
    model: str = Field("gpt-4o-mini")
    vervose: bool = Field(False, description="Whether to use verbose output.")
    
class CorrectTextRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=50000)
    corrections: list[str] = Field(
        default=["fillers", "grammar", "spelling", "punctuation", "style", "formulaic", 
        "triples", "redundancy", "clarity", "coherence", "conciseness", "vocabulary", "tone", "formatting"
        "sentence_variation"],
    )