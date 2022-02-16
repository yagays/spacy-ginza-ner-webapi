from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Named Entity Extraction with Spacy and GiNZA"
    API_V1_STR: str = "/api/v1"

    GINZA_MODEL_NAME: str = "ja_ginza"

    class Config:
        case_sensitive = True


settings = Settings()
