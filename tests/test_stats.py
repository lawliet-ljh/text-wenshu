from datetime import date, datetime

from wenshu_stats.models import Article
from wenshu_stats.stats import index_rate, publish_count_by_editor


def _a(i, editor, ts, indexed=True, pv=100, site="meiyan.com"):
    return Article(i, editor, site, f"t{i}", datetime.fromisoformat(ts), indexed, pv)


def test_publish_count_basic():
    arts = [
        _a(1, "张三", "2026-05-10 10:00:00"),
        _a(2, "张三", "2026-05-11 10:00:00"),
        _a(3, "李四", "2026-05-12 10:00:00"),
        _a(4, "李四", "2026-04-30 10:00:00"),
    ]
    assert publish_count_by_editor(arts, date(2026, 5, 1), date(2026, 5, 20)) == {"张三": 2, "李四": 1}


def test_index_rate():
    arts = [_a(1, "张三", "2026-05-10 10:00:00", True), _a(2, "张三", "2026-05-10 11:00:00", False)]
    assert index_rate(arts) == 0.5
    assert index_rate([]) == 0.0
