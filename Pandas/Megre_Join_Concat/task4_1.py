import pandas as pd

users = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'user_id': [1, 2, 2, 5, 3],
    'amount': [500, 300, 200, 400, 100]
})

print(pd.merge(users, orders, on='user_id', how='inner'))
print(pd.merge(users, orders, on='user_id', how='left'))
print(pd.merge(users, orders, on='user_id', how='right'))
print(pd.merge(users, orders, on='user_id', how='outer'))
print(pd.merge(users, orders, on='user_id', how='inner', indicator=True))