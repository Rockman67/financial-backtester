import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from src.loader.parse_excel import pipeline
import pathlib as pl

def test_parse_basic():
    df = pipeline(pl.Path("samples/input"))
    assert {"Date", "Ticker", "Factor", "Value"}.issubset(df.columns)
    assert len(df) > 1000
    assert df["Value"].notna().all()
