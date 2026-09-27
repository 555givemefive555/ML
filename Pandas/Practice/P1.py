import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'amount': [500, 1200, 300, 700, 1500, 200, 800, 1100, 600, 900],
    'date': pd.to_datetime([
        '2024-01-01', '2024-01-05', '2024-01-10',
        '2024-01-03', '2024-01-07',
        '2024-01-02', '2024-01-06', '2024-01-09',
        '2024-01-04', '2024-01-08'
    ])
})

df1 = df.sort_values(['user_id', 'amount'], ascending=[True, False])
print(df1.groupby('user_id').head(2))