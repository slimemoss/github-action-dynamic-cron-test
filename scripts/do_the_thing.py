#!/usr/bin/env python3
import datetime
import os

# 現在時刻（UTC）を取得
now = datetime.datetime.now(datetime.timezone.utc)

# 今から5分後の時刻を取得
future = now + datetime.timedelta(minutes=5)

# cron形式へ変換（例: 12:05 -> "5 12 * * *"）
cron_expr = f"{future.minute} {future.hour} * * *"

# 出力
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"cron_schedule={cron_expr}\n")
