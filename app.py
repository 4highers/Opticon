"""Creats an FastAPI instance for production/tests"""

from fastapi import APIRouter, FastAPI

from configs.envs import BASE_PATH, DEBUG
from healthz.routers import healthz_router


def create_app() -> FastAPI:
    app = FastAPI(debug=DEBUG,
                  title='Opticon',
                  description='Yet another CMS for blogging.',
                  version='WIP',
                  root_path=BASE_PATH)

    api_v1_router = APIRouter(prefix='/api/v1')
    api_v1_router.include_router(healthz_router)

    app.include_router(api_v1_router)
    return app
