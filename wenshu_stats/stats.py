from datetime import date, datetime, time
from typing import Dict, List

from .models import Article


def _in_range(dt: datetime, start: date, end: date) -> bool:
    """判断发布时间是否落在 [start, end] 日期区间内。"""
    return datetime.combine(start, time.min) <= dt < datetime.combine(end, time.min)


def filter_by_date(articles: List[Article], start: date, end: date) -> List[Article]:
    return [a for a in articles if _in_range(a.published_at, start, end)]


def publish_count_by_editor(articles: List[Article], start: date, end: date) -> Dict[str, int]:
    """统计每个编辑在日期区间内的发文量。"""
    counts: Dict[str, int] = {}
    for a in filter_by_date(articles, start, end):
        counts[a.editor] = counts.get(a.editor, 0) + 1
    return counts


def index_rate(articles: List[Article]) -> float:
    """收录率 = 已收录篇数 / 总篇数，返回 0~1，保留 4 位小数。"""
    if not articles:
        return 0.0
    return round(sum(1 for a in articles if a.indexed) / len(articles), 4)
