from abc import ABC, abstractmethod
from typing import Any, List

import spacy

from app.models.predict import Entity


class BaseMLModel(ABC):
    @abstractmethod
    def predict(self, req: Any) -> Any:
        raise NotImplementedError


class SpacyGinzaNERModel(BaseMLModel):
    def __init__(self, ginza_model_name: str = "ja_ginza") -> None:
        self.nlp = spacy.load(ginza_model_name)

    def predict(self, input_text: str) -> List[Entity]:
        doc = self.nlp(input_text)

        return [Entity(text=e.text, start_char=e.start_char, end_char=e.end_char, label=e.label_) for e in doc.ents]
