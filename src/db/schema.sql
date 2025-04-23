PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS data (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    Date      TEXT    NOT NULL,
    Ticker    TEXT    NOT NULL,
    Factor    TEXT    NOT NULL,
    Value     REAL    NOT NULL,
    Frequency TEXT    NOT NULL CHECK (Frequency IN ('M')),
    Source    TEXT    NOT NULL,
    UNIQUE (Date, Ticker, Factor) ON CONFLICT REPLACE
);

-- ускоряет выборки для Backtrader
CREATE INDEX IF NOT EXISTS idx_data_date_ticker ON data (Date, Ticker);
