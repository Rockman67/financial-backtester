#!/usr/bin/env python
import argparse, pathlib, sys
from src.loader.parse_excel import pipeline
from src.loader.load_data import insert_dataframe
from src.db.init_db import init_db

def cmd_parse(args):
    df = pipeline(args.input)
    if args.dry_run:
        print(df.head())
    if args.save_parquet:
        df.to_parquet("output.parquet", index=False)
        print("Saved output.parquet")
    return df

def cmd_load(args, df=None):
    init_db(args.db)                       # ensure schema
    if df is None:
        df = pipeline(args.input)
    df = df.drop_duplicates(subset=["Date", "Ticker", "Factor"])
    if args.dry_run:
        print(f"Would insert {len(df):,} rows into {args.db}")
    else:
        insert_dataframe(df, args.db)

def main():
    ap = argparse.ArgumentParser(prog="load_data.py")
    sub = ap.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--input", type=pathlib.Path, default="samples/input")
    common.add_argument("--db", type=pathlib.Path, default="db/finance.db")
    common.add_argument("--dry-run", action="store_true")

    # parse
    p = sub.add_parser("parse", parents=[common])
    p.add_argument("--save-parquet", action="store_true")

    # load
    l = sub.add_parser("load", parents=[common])

    # all
    a = sub.add_parser("all", parents=[common])
    a.add_argument("--save-parquet", action="store_true")

    args = ap.parse_args()

    if args.cmd == "parse":
        cmd_parse(args)
    elif args.cmd == "load":
        cmd_load(args)
    elif args.cmd == "all":
        df = cmd_parse(args)
        cmd_load(args, df)

if __name__ == "__main__":
    main()
