import pandas as pd

data = {'이름' : ['카리나', '윈터', '닝닝', '지젤'],
        '나이' : [25, 22, 29, 31],
        '생일' : ['2000-06-21', '2000-07-08', '2000-03-04', '1990-02-12']}
df1 = pd.DataFrame(data)

# 새로운 데이터를 여러개 추가 할땐 concat 함수를 사용
new_data = pd.DataFrame({'이름': ['신입1', '신입2'], '나이': [26, 27], '생일': ['1995-01-01', '1996-02-02']})
df1 = pd.concat([df1, new_data], ignore_index=True)

print(df1)
