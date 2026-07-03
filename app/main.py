from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="API REST para gerenciamento de atividades.",
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/", tags=["status"])
def root() -> dict[str, str]:
    return {
        "message": "Tasks API no ar",
        "docs": "/docs",
        "health": f"{settings.api_prefix}/health",
    }
