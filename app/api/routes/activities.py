from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.crud.activity import (
    create_activity,
    delete_activity,
    get_activity,
    list_activities,
    update_activity,
)
from app.schemas.activity import ActivityCreate, ActivityRead, ActivityUpdate

router = APIRouter()


@router.post("", response_model=ActivityRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ActivityCreate, db: Session = Depends(get_db)) -> ActivityRead:
    return create_activity(db=db, payload=payload)


@router.get("", response_model=list[ActivityRead])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[ActivityRead]:
    return list_activities(db=db, skip=skip, limit=limit)


@router.get("/{activity_id}", response_model=ActivityRead)
def read_item(activity_id: str, db: Session = Depends(get_db)) -> ActivityRead:
    activity = get_activity(db=db, activity_id=activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Atividade nao encontrada")
    return activity


@router.patch("/{activity_id}", response_model=ActivityRead)
def patch_item(
    activity_id: str,
    payload: ActivityUpdate,
    db: Session = Depends(get_db),
) -> ActivityRead:
    activity = update_activity(db=db, activity_id=activity_id, payload=payload)
    if activity is None:
        raise HTTPException(status_code=404, detail="Atividade nao encontrada")
    return activity


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(activity_id: str, db: Session = Depends(get_db)) -> None:
    deleted = delete_activity(db=db, activity_id=activity_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Atividade nao encontrada")
