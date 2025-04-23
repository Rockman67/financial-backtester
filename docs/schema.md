# Data Table Schema (Stage 1)

> Version 0.1 – 2025-04-23

## Table `data`

| Field | Type | Example | Note |
|-------|------|---------|------|
| Date | TEXT | 2019-01-29 | ISO `YYYY-MM-DD` |
| Ticker | TEXT | SASE:4001 | Security identifier |
| Factor | TEXT | PE_LTM | Short factor name |
| Value | REAL | 17.33 | Numeric factor value |
| Frequency | TEXT | M | `M` = monthly |
| Source | TEXT | CapitalIQ | Data origin |

```
+-----------+
|  data     |
+-----------+
| id (PK)   |
| Date      |
| Ticker    |
| Factor    |
| Value     |
| Frequency |
| Source    |
+-----------+
```

## Mapping — file “1) database (Formula).xlsx” (sheet `Price_Wide`)

| Excel Column | Factor Name | Note |
|--------------|-------------|------|
| `Price` | PRICE | Higher worse |
| `Volume (5D_Avg)` | VOLUME_5D | — |
| `EV/EBITDA` | EV_EBITDA | Lower better |
