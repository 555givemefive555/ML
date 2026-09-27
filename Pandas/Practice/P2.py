import pandas as pd

df = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5],
    'order_date': pd.to_datetime([
        '2024-01-05', '2024-01-20', '2024-02-10',
        '2024-01-15', '2024-02-25',
        '2024-02-01', '2024-03-05', '2024-03-20',
        '2024-02-15', '2024-03-10',
        '2024-03-25'
    ]),
    'amount': [500, 700, 300, 800, 600, 400, 900, 200, 1000, 500, 700]
})

df['order_month_num'] = df['order_date'].dt.year * 12 + df['order_date'].dt.month
df['cohort_month_num'] = df.groupby('user_id')['order_month_num'].transform('min')
df['month_number'] = df['order_month_num'] - df['cohort_month_num']
df['cohort_month'] = df.groupby('user_id')['order_date'].transform('min').dt.to_period('M')
result = (
    df.groupby(['user_id', 'cohort_month', 'month_number'])
      .size()
      .reset_index(name='n_orders')
      .sort_values(['user_id', 'month_number'])
)

print(result)