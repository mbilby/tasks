from fastapi import APIRouter

from app.api.routes.activities import router as activities_router

api_router = APIRouter()

api_router.include_router(activities_router, prefix="/activities", tags=["activities"])


@api_router.get("/health", tags=["status"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
