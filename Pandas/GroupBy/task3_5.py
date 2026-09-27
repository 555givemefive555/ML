import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 2, 3, 3],
    'amount': [100, 200, 150, 300, 50, 400, 100]
})

total_amount = df.groupby('user_id').agg(
    total_amount = ('amount', 'sum')
    )
n_purchase = df.groupby('user_id').agg(
    n_purchase = ('amount', 'size')
    )

df = pd.merge(df, total_amount, on='user_id', how='left')
df = pd.merge(df, n_purchase, on='user_id', how='left')
print(df[df['amount'] > (0.5 * df['total_amount'])])