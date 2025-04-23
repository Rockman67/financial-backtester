import sys, pathlib, sqlite3
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.db.init_db import init_db  # ← добавим функцию-обёртку
from src.loader.parse_excel import pipeline
from src.loader.load_data import insert_dataframe

def test_insert_and_dedup(tmp_path):
    db = tmp_path / "test.db"

    # 1) создаём схему таблицы
    init_db(db)

    # 2) берём маленький сэмпл данных
    sample_df = pipeline(pathlib.Path("samples/input")).head(1000)

    # 3) вставляем дважды
    insert_dataframe(sample_df, db)
    insert_dataframe(sample_df, db)

    # 4) проверяем, что дубликаты не удвоились
    with sqlite3.connect(db) as conn:
        rows = conn.execute("SELECT COUNT(*) FROM data").fetchone()[0]

    unique_rows = len(sample_df.drop_duplicates(subset=["Date", "Ticker", "Factor"]))
    assert rows == unique_rows
