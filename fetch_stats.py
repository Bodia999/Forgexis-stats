from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SERVICE_ACCOUNT_FILE = 'service_account.json'
SITE_URL = 'https://bodia999.github.io/Forgexis/'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

webmasters = build('searchconsole', 'v1', credentials=credentials)

# Запрашиваем данные за последние 7 дней
request = {
    'startDate': '2026-01-08',
    'endDate': '2026-01-15',
    'dimensions': ['date']
}

response = webmasters.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()

clicks = sum(row['clicks'] for row in response.get('rows', []))
impressions = sum(row['impressions'] for row in response.get('rows', []))
ctr = round((clicks / impressions * 100) if impressions else 0, 2)

stats = {
    "clicks": clicks,
    "impressions": impressions,
    "ctr": ctr,
    "avg_position": 0.0
}

with open('stats.json', 'w') as f:
    json.dump(stats, f)
