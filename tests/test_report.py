from datetime import datetime

from wenshu_stats.models import Article
from wenshu_stats.report import build_editor_report


def _a(i, editor, indexed, pv):
    return Article(i, editor, "meiyan.com", f"t{i}", datetime(2026, 5, 1, 10), indexed, pv)


def test_editor_report():
    arts = [_a(1, "李四", True, 100), _a(2, "张三", False, 300), _a(3, "张三", True, 50)]
    rows = build_editor_report(arts)
    assert [r["editor"] for r in rows] == ["张三", "李四"]
    assert rows[0] == {
        "editor": "张三", "total": 2, "indexed": 1, "index_rate": 0.5,
        "pv_sum": 350, "avg_pv": 175.0, "top_title": "t2",
    }
