import argparse
import csv
import sys
from datetime import date

from .loader import load_articles
from .report import build_editor_report
from .stats import filter_by_date, index_rate, publish_count_by_editor


def _parse_date(s: str) -> date:
    return date.fromisoformat(s)


def cmd_summary(args) -> None:
    articles = load_articles(args.file)
    counts = publish_count_by_editor(articles, args.start, args.end)
    in_range = filter_by_date(articles, args.start, args.end)
    print(f"区间 {args.start} ~ {args.end}  发文 {len(in_range)} 篇  收录率 {index_rate(in_range):.2%}")
    for editor, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{editor}\t{n}")


def cmd_report(args) -> None:
    articles = filter_by_date(load_articles(args.file), args.start, args.end)
    rows = build_editor_report(articles)
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()) if rows else ["editor"])
    writer.writeheader()
    writer.writerows(rows)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="wenshu_stats", description="文枢发文统计")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name, func in (("summary", cmd_summary), ("report", cmd_report)):
        p = sub.add_parser(name)
        p.add_argument("file")
        p.add_argument("--from", dest="start", type=_parse_date, required=True)
        p.add_argument("--to", dest="end", type=_parse_date, required=True)
        p.set_defaults(func=func)
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
