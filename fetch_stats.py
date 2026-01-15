import json
import datetime

# Пример: сюда можно поставить логику для получения статистики
# Например, через Google Search Console API
# Пока для теста используем случайные данные

import random

clicks = random.randint(100, 500)
impressions = random.randint(1000, 2000)
ctr = round(clicks / impressions * 100, 2)
avg_position = round(random.uniform(1, 5), 2)

stats = {
    "clicks": clicks,
    "impressions": impressions,
    "ctr": ctr,
    "avg_position": avg_position,
    "last_updated": str(datetime.datetime.now())
}

with open('stats.json', 'w') as f:
    json.dump(stats, f, indent=4)
