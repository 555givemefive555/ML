import pandas as pd

users = pd.DataFrame({
    'user_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
}).set_index('user_id')

orders = pd.DataFrame({
    'amount': [500, 300, 200]
}, index=[1, 2, 5])

print(users.join(orders))
print(users.join(orders, how='inner'))
print(users.join(orders, how='outer'))