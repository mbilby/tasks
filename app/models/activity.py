from __future__ import annotations

import enum
from datetime import date

from datetime import date

from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ActivityStatus(str, enum.Enum):
    pendente = "pendente"
    em_andamento = "em_andamento"
    concluida = "concluida"
    cancelada = "cancelada"


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    agente_responsavel: Mapped[str] = mapped_column(String(120), nullable=False)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    data_conclusao: Mapped[date | None] = mapped_column(Date, nullable=True)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default=ActivityStatus.pendente.value,
        server_default=ActivityStatus.pendente.value,
    )
