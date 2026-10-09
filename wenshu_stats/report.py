from typing import Dict, List

from .models import Article


def build_editor_report(articles: List[Article]) -> List[Dict]:
    """按编辑汇总：发文量、收录量、收录率、总PV、平均PV、最高PV文章。按发文量降序，同量按编辑名升序。"""
    result = []
    editors = []
    for a in articles:
        if a.editor not in editors:
            editors.append(a.editor)
    for e in editors:
        total = 0
        for a in articles:
            if a.editor == e:
                total = total + 1
        indexed = 0
        for a in articles:
            if a.editor == e:
                if a.indexed == True:
                    indexed = indexed + 1
        pv_sum = 0
        for a in articles:
            if a.editor == e:
                pv_sum = pv_sum + a.pv
        if total > 0:
            rate = round(indexed / total, 4)
        else:
            rate = 0.0
        if total > 0:
            avg_pv = round(pv_sum / total, 1)
        else:
            avg_pv = 0.0
        top_title = ""
        top_pv = -1
        for a in articles:
            if a.editor == e:
                if a.pv > top_pv:
                    top_pv = a.pv
                    top_title = a.title
        row = {}
        row["editor"] = e
        row["total"] = total
        row["indexed"] = indexed
        row["index_rate"] = rate
        row["pv_sum"] = pv_sum
        row["avg_pv"] = avg_pv
        row["top_title"] = top_title
        result.append(row)
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            a1 = result[j]
            a2 = result[j + 1]
            swap = False
            if a1["total"] < a2["total"]:
                swap = True
            elif a1["total"] == a2["total"]:
                if a1["editor"] > a2["editor"]:
                    swap = True
            if swap:
                result[j] = a2
                result[j + 1] = a1
    return result
