from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    id: int
    editor: str
    site: str
    title: str
    published_at: datetime
    indexed: bool  # 是否已被百度收录
    pv: int
