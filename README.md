```markdown
# Financial-Backtester – Stages 1 & 2

Automated pipeline that

1. **Stage 1:** loads & normalises Capital IQ Excel files → SQLite  
2. **Stage 2:** streams data into Backtrader, runs factor strategy, performs grid-search

---

## 1 Requirements

```bash
Python >= 3.12
pip install -r requirements.txt
```

Libraries added in Stage 2: `backtrader 1.9.78`, `SQLAlchemy`, `PyYAML`, `numexpr`,  
plus optional `matplotlib` (for local charts).

---

## 2 Repository layout

```
financial-backtester/
├── configs/                # YAML presets (single run & grid search)
├── db/                     # ← finance.db is generated, NOT stored in Git
├── results/                # auto-generated equity_* / grid_*.csv
├── samples/input/          # raw CapitalIQ Excel dumps
├── src/
│   ├── db/                 # schema + init_db.py
│   ├── loader/             # Excel → SQLite (Stage 1)
│   ├── feeds/sqlite_feed.py   # SQLite → Backtrader (Stage 2)
│   ├── strategies/factor_strategy.py
│   └── filters/            # expr, cross-sectional, time-series filters
├── run_bt.py               # single back-test launcher
├── grid_search.py          # parameter sweep wrapper
├── validate_data.py        # quick NA / outlier report
└── tests/                  # 9 pytest unit-tests
```

---

## 3 Quick start

### 3.1  Build / refresh database  (Stage 1)

```bash
# create SQLite schema
python src/db/init_db.py

# dry-run to preview unique rows
python load_data.py all --input samples/input --dry-run

# real import
python load_data.py all --input samples/input
```

### 3.2  Run a single back-test  (Stage 2)

```bash
# using preset YAML
python run_bt.py --config configs/demo.yml

# or ad-hoc flags
python run_bt.py --ticker SASE:1010 --from 2019-01-01 --to 2025-03-25 ^
                 --factor pb:-1
```

*Outputs* → `results/equity_<ticker>.csv`

### 3.3  Grid-search (6 combos in the demo)

```bash
python grid_search.py --config configs/grid_demo.yml
# results/grid_YYYYMMDD_HHMM.csv is produced
```

### 3.4  Validate data quality

```bash
python validate_data.py db/finance.db --summary
```

---

## 4 What happens under the hood?

1. **SQLiteFeed** pivots `(Date, Ticker, Factor, Value)` rows → wide dataframe,  
   auto-adds missing factor columns as NaN.  
2. **FactorStrategy**  
   * computes weighted score (e.g. `pb × –1`)  
   * applies expression filter (`pe < 15` in demo) + optional cross-section & TS filters  
   * rebalances monthly or quarterly.  
3. Backtrader logs portfolio value each bar; CSV is later visualised or fed to Stage 3 (web UI).  
4. `grid_search.py` iterates over parameter grid, computes CAGR / Sharpe / MaxDD for each run.

---

## 5 Test suite

```bash
pytest -q      # 9 tests: parser, feed, expr, cross, ts filters
```

All tests pass ✔.

---

## 6 CLI reference

```bash
# Stage 1 helpers
python load_data.py --help
python src/db/init_db.py --help

# Stage 2 helpers
python run_bt.py --help
python grid_search.py --help
python validate_data.py --help
```

---

*Stage 2 completed – repository tag **v0.2-stage2**.*  
Next milestone: Stage 3 – minimal Flask web dashboard.
```
