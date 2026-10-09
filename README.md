# text-wenshu

文枢发文统计小工具（Cline Cloud Agents 测试用项目）。

## 运行

```bash
pip install -r requirements.txt
python -m wenshu_stats summary data/sample_articles.csv --from 2026-05-01 --to 2026-05-31
python -m wenshu_stats report  data/sample_articles.csv --from 2026-05-01 --to 2026-05-31
pytest -q
```

## 结构

- `wenshu_stats/models.py`：文章数据结构
- `wenshu_stats/loader.py`：从 CSV 读取文章
- `wenshu_stats/stats.py`：日期过滤、发文量、收录率
- `wenshu_stats/report.py`：按编辑汇总报表
- `wenshu_stats/cli.py`：命令行入口
- `data/sample_articles.csv`：样例数据
