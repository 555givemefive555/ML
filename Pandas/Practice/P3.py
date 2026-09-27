import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    'order_date': pd.to_datetime([
        '2023-12-01', '2024-01-15', '2024-03-20',
        '2024-02-10', '2024-03-25',
        '2024-01-05', '2024-02-15', '2024-03-30',
        '2024-01-20', '2024-02-25', '2024-03-15',
        '2024-03-28'
    ]),
    'amount': [500, 700, 300, 800, 600, 400, 900, 200, 1000, 500, 300, 700]
})

today = pd.to_datetime('2024-04-01')
df1 = (df.groupby('user_id').agg(
    R=('order_date', 'max'),
    F=('amount', 'size'),
    M=('amount', 'sum')
    )).reset_index()
df1['R'] = (today - df1['R'])
print(df1)