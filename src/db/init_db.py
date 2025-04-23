# src/db/init_db.py
# ───────────────────────────────────────────────────────────
# Single-purpose helper to create (or upgrade) SQLite schema
# for the project. It can be invoked either:
#
#   python src/db/init_db.py                 → uses default path db/finance.db
#   >>> from src.db.init_db import init_db
#   >>> init_db("tmp/test.db")               → any custom path (used in tests)

import sqlite3
import pathlib
import sys

# ───────────────────────────────────────────────────────────
# Internal helper (DO NOT import directly from tests)
# -----------------------------------------------------------------
def _create_schema(db_file: pathlib.Path) -> None:
    """Executes schema.sql against *db_file*."""
    db_file.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_file) as conn, open("src/db/schema.sql", encoding="utf-8") as f:
        conn.executescript(f.read())


# ───────────────────────────────────────────────────────────
# Public function — import in tests or other modules
# -----------------------------------------------------------------
def init_db(path: str | pathlib.Path = "db/finance.db") -> pathlib.Path:
    """
    Create (or upgrade) a SQLite database at *path* using schema.sql
    and return the resolved path object.
    """
    db_file = pathlib.Path(path)
    _create_schema(db_file)
    return db_file.resolve()


# ───────────────────────────────────────────────────────────
# CLI entry-point
# -----------------------------------------------------------------
if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("db/finance.db")
    init_db(target)
    print("DB created at", target.resolve())
