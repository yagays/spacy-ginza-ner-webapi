from typing import Callable

from fastapi import FastAPI

from app.services.model import SpacyGinzaNERModel


def _startup_model(app: FastAPI, ginza_model_name: str) -> None:
    model_instance = SpacyGinzaNERModel(ginza_model_name)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI, ginza_model_name: str) -> Callable:
    def startup() -> None:
        _startup_model(app, ginza_model_name)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)

    return shutdown
