# week6_lab.py
# Author: Jason Nguyen

records = [
    {
        "id": 1,
        "name": "Dell Laptop",
        "category": "Laptop",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "HP Laptop",
        "category": "Laptop",
        "amount": 700,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "MacBook",
        "category": "Laptop",
        "amount": 1500,
        "status": "Approved",
    },
    {
        "id": 4,
        "name": "Lenovo Laptop",
        "category": "Laptop",
        "amount": 850,
        "status": "Pending",
    },
    {
        "id": 5,
        "name": "Gaming Laptop",
        "category": "Laptop",
        "amount": 2200,
        "status": "Pending",
    },
]

LIMIT = 1000
HIGH = 2000

total = 0
flagged = []
high_value = []

for rec in records:
    if rec["status"] == "Pending":
        total += rec["amount"]

        if rec["amount"] > LIMIT:
            flagged.append(rec)

        if rec["amount"] > HIGH:
            high_value.append(rec)

import os

os.makedirs("data", exist_ok=True)

lines = [
    f"Pending total:   ${total:,.2f}",
    f"Needs review:    {len(flagged)}",
    f"High-value:      {len(high_value)}",
]

for line in lines:
    print(line)

with open("data/week6_summary.txt", "w") as f:
    f.write("\n".join(lines) + "\n")

print("\nRecords needing review:")
for r in flagged:
    print(f"  ID {r['id']}: {r['name']} - ${r['amount']:,.2f}")
