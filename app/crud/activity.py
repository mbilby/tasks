from __future__ import annotations

from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.activity import Activity, ActivityStatus
from app.schemas.activity import ActivityCreate, ActivityUpdate
from app.services.hash_id import generate_activity_id


def create_activity(db: Session, payload: ActivityCreate) -> Activity:
    activity = Activity(
        id=generate_activity_id(payload.titulo, payload.agente_responsavel),
        titulo=payload.titulo,
        agente_responsavel=payload.agente_responsavel,
        data_inicio=payload.data_inicio,
        data_conclusao=payload.data_conclusao
        or (date.today() if payload.status == ActivityStatus.concluida else None),
        descricao=payload.descricao,
        status=payload.status,
    )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


def list_activities(db: Session, skip: int = 0, limit: int = 100) -> list[Activity]:
    statement = select(Activity).order_by(Activity.data_inicio.desc()).offset(skip).limit(limit)
    return list(db.scalars(statement).all())


def get_activity(db: Session, activity_id: str) -> Activity | None:
    return db.get(Activity, activity_id)


def update_activity(db: Session, activity_id: str, payload: ActivityUpdate) -> Activity | None:
    activity = db.get(Activity, activity_id)
    if activity is None:
        return None

    data = payload.model_dump(exclude_unset=True)
    if not data:
        return activity

    for field, value in data.items():
        setattr(activity, field, value)

    if activity.status == ActivityStatus.concluida and activity.data_conclusao is None:
        activity.data_conclusao = date.today()

    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


def delete_activity(db: Session, activity_id: str) -> bool:
    activity = db.get(Activity, activity_id)
    if activity is None:
        return False

    db.delete(activity)
    db.commit()
    return True
