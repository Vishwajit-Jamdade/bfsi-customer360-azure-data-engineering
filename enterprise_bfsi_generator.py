"""
Enterprise BFSI Dataset Generator
Generates:
- 100K Customers
- 150K Accounts
- 50K Loans
- 80K Credit Cards
- 25K Complaints
- 2M Transactions (chunked)
"""

from faker import Faker
import pandas as pd
import random
import os

fake = Faker("en_IN")
random.seed(42)

BASE_DIR = "generated_bfsi_data"
os.makedirs(BASE_DIR, exist_ok=True)

CUSTOMERS = 100000
ACCOUNTS = 150000
LOANS = 50000
CARDS = 80000
COMPLAINTS = 25000
TRANSACTIONS = 2000000

print("Generating Customers...")
customers = []
for i in range(1, CUSTOMERS + 1):
    customers.append([
        f"CUST{i:06d}",
        fake.first_name(),
        fake.last_name(),
        fake.city(),
        random.choice(["Maharashtra","Karnataka","Gujarat","Delhi","Tamil Nadu"]),
        random.randint(300000, 3000000)
    ])

pd.DataFrame(customers, columns=[
    "customer_id","first_name","last_name","city","state","annual_income"
]).to_csv(f"{BASE_DIR}/customers.csv", index=False)

print("Generating Accounts...")
accounts = []
for i in range(1, ACCOUNTS + 1):
    accounts.append([
        f"ACC{i:06d}",
        f"CUST{random.randint(1,CUSTOMERS):06d}",
        random.choice(["SAVINGS","CURRENT","SALARY"]),
        random.randint(1000,500000)
    ])

pd.DataFrame(accounts, columns=[
    "account_id","customer_id","account_type","balance"
]).to_csv(f"{BASE_DIR}/accounts.csv", index=False)

print("Generating Loans...")
loans = []
for i in range(1, LOANS + 1):
    loans.append([
        f"LOAN{i:06d}",
        f"CUST{random.randint(1,CUSTOMERS):06d}",
        random.choice(["HOME","CAR","PERSONAL","BUSINESS"]),
        random.randint(100000,5000000)
    ])

pd.DataFrame(loans, columns=[
    "loan_id","customer_id","loan_type","loan_amount"
]).to_csv(f"{BASE_DIR}/loans.csv", index=False)

print("Generating Credit Cards...")
cards = []
for i in range(1, CARDS + 1):
    cards.append([
        f"CARD{i:06d}",
        f"CUST{random.randint(1,CUSTOMERS):06d}",
        random.choice(["SILVER","GOLD","PLATINUM"]),
        random.randint(50000,1000000)
    ])

pd.DataFrame(cards, columns=[
    "card_id","customer_id","card_type","credit_limit"
]).to_csv(f"{BASE_DIR}/credit_cards.csv", index=False)

print("Generating Complaints...")
complaints = []
for i in range(1, COMPLAINTS + 1):
    complaints.append([
        f"COMP{i:06d}",
        f"CUST{random.randint(1,CUSTOMERS):06d}",
        random.choice(["CARD_ISSUE","LOAN_ISSUE","UPI_ISSUE","FRAUD_ALERT"]),
        random.choice(["OPEN","CLOSED"])
    ])

pd.DataFrame(complaints, columns=[
    "complaint_id","customer_id","complaint_type","status"
]).to_csv(f"{BASE_DIR}/complaints.csv", index=False)

print("Generating Transactions (chunked)...")
chunk_size = 100000
for start in range(1, TRANSACTIONS + 1, chunk_size):
    rows = []
    end = min(start + chunk_size - 1, TRANSACTIONS)
    for i in range(start, end + 1):
        rows.append([
            f"TXN{i:08d}",
            f"ACC{random.randint(1,ACCOUNTS):06d}",
            random.choice(["DEBIT","CREDIT","UPI","TRANSFER"]),
            random.randint(10,50000)
        ])

    pd.DataFrame(rows, columns=[
        "transaction_id","account_id","transaction_type","amount"
    ]).to_csv(
        f"{BASE_DIR}/transactions_{start}_{end}.csv",
        index=False
    )
    print(f"Written {start} to {end}")

print("Done.")
