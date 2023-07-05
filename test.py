df1 = pd.DataFrame({
    'name': ['Mike', 'Sam', 'Bill'],
    'age': [23, 25, 29],
    'height': [176, 192, 182]
})

df2 = pd.DataFrame({
    'name': ['Mike', 'John', 'Bill'],
    'salary': [100, 120, 150],
    'tax': [0, 13, 0]
})
df3 = df1.join(df2, on='name', how='inner')
print(df3)