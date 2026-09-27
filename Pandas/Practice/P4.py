import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5],
    'month': ['2024-01', '2024-02', '2024-03',
              '2024-01', '2024-02',
              '2024-02', '2024-03',
              '2024-01', '2024-03', '2024-04',
              '2024-04']
})

today = pd.to_datetime('2024-05')
df1 = pd.DataFrame()
df1 = (df.groupby('user_id').agg(last_month=('month', 'max'))).reset_index()
df1 = df1.sort_values('user_id')
df1['last_month'] = pd.to_datetime(df1['last_month'])
df1['months_since_last'] = ((today.year - df1['last_month'].dt.year)*12 + today.month - df1['last_month'].dt.month)
df1['is_churned'] = df1['months_since_last'] > 1
print(df1)
print((df1['months_since_last'] > 1).sum())
ans = df1[df1['is_churned']]['last_month'].mean().strftime('%Y-%m')
print(ans)