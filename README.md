
# Financial Backtester – Stage 1

Automated **Data Loading & Processing** pipeline.

## 1 Requirements
```bash
Python >= 3.12
pip install -r requirements.txt
```

## 2 Folder layout
```
financial-backtester/
├── samples/input/        # raw Excel files
├── db/finance.db         # SQLite database (auto‑created)
├── src/                  # parser / loader code
└── load_data.py          # CLI wrapper
```

## 3 Quick Start (3 steps)
```bash
# 1 Create / upgrade DB schema
python src/db/init_db.py

# 2 Parse Excel → preview unique rows
python load_data.py all --input samples/input --dry-run

# 3 Real import
python load_data.py all --input samples/input
```

### Commands reference
```bash
python load_data.py --help

python load_data.py parse --input samples/input --save-parquet
python load_data.py load  --db db/finance.db
```

## 4 What happens?
1. **parse** – converts every `*.xlsx` to long format  
   (`Date, Ticker, Factor, Value, Frequency, Source`).
2. **load** – deduplicates by `(Date, Ticker, Factor)` and writes to SQLite  
   (`ON CONFLICT REPLACE`). Duplicates reported & skipped.

## 5 Run tests
```bash
pytest -q    # parse, load and CLI smoke tests
```

---
