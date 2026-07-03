from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from uuid import uuid4


def generate_activity_id(titulo: str, agente_responsavel: str) -> str:
    seed = f"{titulo}|{agente_responsavel}|{datetime.now(timezone.utc).isoformat()}|{uuid4().hex}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()
