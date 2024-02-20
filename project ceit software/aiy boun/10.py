data = [
    {
        "created_at": "2024-07-29T03:03:42Z",
        "amount": 4834810
    },
    {
        "created_at": "2024-03-13T09:18:49Z",
        "amount": 3435464
    },....]

total_income = 0
total_expense = 0

for item in data:
    if item['amount'] > 0:
        total_income += item['amount']
    else:
        total_expense += abs(item['amount'])

print("ລາຍຮັບທັງໝົດ:", total_income)
print("ລາຍຈ່າຍທັງໝົດ:", total_expense)
