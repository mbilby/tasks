"""create activities table

Revision ID: 0001_create_activities_table
Revises:
Create Date: 2026-07-01 00:00:00
"""

from alembic import op
import sqlalchemy as sa


revision = "0001_create_activities_table"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "activities",
        sa.Column("id", sa.String(length=64), primary_key=True, nullable=False),
        sa.Column("titulo", sa.String(length=200), nullable=False),
        sa.Column("agente_responsavel", sa.String(length=120), nullable=False),
        sa.Column("data_inicio", sa.Date(), nullable=False),
        sa.Column("data_conclusao", sa.Date(), nullable=True),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
            server_default=sa.text("'pendente'"),
        ),
    )


def downgrade() -> None:
    op.drop_table("activities")
