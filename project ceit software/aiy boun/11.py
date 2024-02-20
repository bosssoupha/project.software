import json
from collections import defaultdict
from datetime import datetime

data =   [
    {
        "created_at": "2024-07-29T03:03:42Z",
        "amount": 4834810
    },.... ຂຽນຕໍ່ເອງ
    {
        "created_at": "2024-03-13T09:18:49Z",
        "amount": 3435464
    },
 ]

monthly_summary = defaultdict(lambda: {'income': 0, 'expense': 0})

for item in data:
    created_at = datetime.fromisoformat(item['created_at'].replace('Z', '+00:00'))
    month = created_at.strftime('%Y-%m')
    if item['amount'] > 0:
        monthly_summary[month]['income'] += item['amount']
    else:
        monthly_summary[month]['expense'] += abs(item['amount'])

for month, summary in monthly_summary.items():
    print(f"ເດືອນ {month}:")
    print(f"   ລາຍຮັບ: {summary['income']}")
    print(f"   ລາຍຈ່າຍ: {summary['expense']}")
