#!/bin/bash
# Backup da base Tasks via pg_dump no container Docker
# Uso: ./backup.sh [diretorio_destino]

set -euo pipefail

DEST="${1:-/home/openclaw/backups/tasks-api}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${DEST}/tasks_${TIMESTAMP}.sql.gz"

mkdir -p "$DEST"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Iniciando backup -> $BACKUP_FILE"

sg docker -c "docker exec tasks-postgres pg_dump -U tasks -d Tasks --no-owner --no-privileges" 2>/dev/null | gzip > "$BACKUP_FILE"

# Validação básica: arquivo não vazio e com pelo menos 50 bytes
if [ -s "$BACKUP_FILE" ] && [ "$(stat -c%s "$BACKUP_FILE")" -gt 50 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Backup concluido: $(stat -c%s "$BACKUP_FILE") bytes"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERRO: arquivo de backup vazio ou invalido"
    rm -f "$BACKUP_FILE"
    exit 1
fi

# Manter apenas os ultimos 14 backups
ls -t "$DEST"/tasks_*.sql.gz 2>/dev/null | tail -n +15 | while read -r old; do
    rm -f "$old"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Removido backup antigo: $old"
done