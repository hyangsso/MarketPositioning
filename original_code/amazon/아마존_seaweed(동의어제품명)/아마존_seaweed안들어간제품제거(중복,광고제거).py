import pandas as pd

#remove duplicate product name from the list 중복제거
df = pd.read_excel("merged_seaweed_words.xlsx", usecols = ['product_name'])
print(df)

df2 = df.drop_duplicates(subset= ['product_name'], keep="first")
df3 = df2[df2.product_name.str.contains('Seaweed','seaweed')]
print(df3)
df3.to_excel("no_dup_merged_seaweed_words.xlsx")
