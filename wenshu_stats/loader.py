import csv
from datetime import datetime
from typing import List

from .models import Article


def load_articles(path: str) -> List[Article]:
    articles = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            articles.append(
                Article(
                    id=int(row["id"]),
                    editor=row["editor"],
                    site=row["site"],
                    title=row["title"],
                    published_at=datetime.strptime(row["published_at"], "%Y-%m-%d %H:%M:%S"),
                    indexed=row["indexed"] == "1",
                    pv=int(row["pv"]),
                )
            )
    return articles
