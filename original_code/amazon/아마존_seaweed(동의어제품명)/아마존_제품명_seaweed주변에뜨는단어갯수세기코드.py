import pandas as pd

#count # of each date repeat

df = pd.read_csv("seaweed_-1_+1_with.csv", usecols = ['words'])


dups_date = df.pivot_table(index = ['words'], aggfunc = 'size')
dups_date.to_excel("merged_seaweed_-1_+1.xlsx")