import pandas as pd

df = pd.DataFrame({
    'order_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5],
    'product': ['bread', 'milk', 'eggs',
                'bread', 'butter',
                'milk', 'eggs', 'butter',
                'bread', 'milk',
                'eggs']
})

df1 = df.merge(df, on='order_id')
df1 = df1[df1['product_x'] < df1['product_y']]
df1 = df1.groupby(['product_x', 'product_y']).agg(
    count_of_pairs=('order_id', 'size')).reset_index()
df1 = df1[df1['count_of_pairs'] > 1]
print(df1.sort_values('count_of_pairs', ascending=False))