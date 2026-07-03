from __future__ import annotations

from datetime import date
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from app.models.activity import ActivityStatus


class ActivityBase(BaseModel):
    titulo: Annotated[str, Field(min_length=3, max_length=200)]
    agente_responsavel: Annotated[str, Field(min_length=2, max_length=120)]
    data_inicio: date
    data_conclusao: date | None = None
    descricao: str | None = Field(default=None, max_length=5000)
    status: ActivityStatus = ActivityStatus.pendente


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    titulo: Annotated[str | None, Field(min_length=3, max_length=200)] = None
    agente_responsavel: Annotated[str | None, Field(min_length=2, max_length=120)] = None
    data_inicio: date | None = None
    data_conclusao: date | None = None
    descricao: str | None = Field(default=None, max_length=5000)
    status: ActivityStatus | None = None


class ActivityRead(ActivityBase):
    id: str

    model_config = ConfigDict(from_attributes=True)
