from typing import Any

from fastapi import APIRouter, Request

from app.models.predict import PredictRequest, PredictResponse

api_router = APIRouter()


@api_router.post("/predict", response_model=PredictResponse)
async def predict(request: Request, payload: PredictRequest) -> Any:
    """
    NER
    """
    input_text = payload.input_text
    model = request.app.state.model

    ents = model.predict(input_text)
    return PredictResponse(text=input_text, ents=ents)
