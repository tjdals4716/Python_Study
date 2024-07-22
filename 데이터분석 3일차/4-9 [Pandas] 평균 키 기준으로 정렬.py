import pandas as pd

filename = '/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/CSV/singerA.csv'
df = pd.read_csv(filename, index_col=None, encoding='CP949')

df_sort1 = df.sort_values(by=['평균 키'], axis=0)
print(df_sort1)