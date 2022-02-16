from typing import List

from pydantic import BaseModel, Field, StrictStr


class Entity(BaseModel):
    text: str = Field(..., title="Text", description="Entity Text.", example="Apple")
    start_char: int = Field(
        ..., title="Start char", description="The character offset for the start of the span.", example=0
    )
    end_char: int = Field(..., title="End char", description="The character offset for the end of the span.", example=4)
    label: str = Field(..., title="Label", description="Entity label.", example="ORG")


class PredictRequest(BaseModel):
    input_text: StrictStr = Field(..., title="input_text", description="Input text", example="Input text for ML")


class PredictResponse(BaseModel):
    text: StrictStr = Field(
        ...,
        title="input_text",
        description="Same as request text",
        example="Apple is looking at buying U.K. startup for $1 billion",
    )
    ents: List[Entity]
