import pandas as pd

df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [5, 6], 'b': [7, 8]})
df3 = pd.DataFrame({'a': [5, 6], 'c': [7, 8]})

print(pd.concat((df1, df2), axis=0))
print(pd.concat((df1, df2), axis=1))
print(pd.concat((df1, df3), axis=0))
print(pd.concat((df1, df2), axis=0, ignore_index=True))