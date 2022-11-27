import numpy as np
import pandas as pd
import datetime as dt
import openpyxl

data = [[dt.datetime(2020,1,1,10,13), 2.222, 1, True],
        [dt.datetime(2020,1,2),np.nan, 2, False],
        [dt.datetime(2020,1,2),np.inf, 3, True]]

df = pd.DataFrame(data=data, columns = ['Dates', 'Floats', 'Integers', 'Booleans'])
df.index.name='index'
print(df)
df.to_excel('written_with_pandas3.xlsx', sheet_name='Output', startrow=1, index=True, header=True,na_rep='<NA>', inf_rep='<INF>')
# with pd.ExcelWriter('written_with_pandas.xlsx') as writer:
#         df.to_excel(writer, sheet_name='Sheet1', startrow=1, startcol=1)
#         df.to_excel(writer, sheet_name='Sheet1', startrow=10, startcol=1)
#         df.to_excel(writer, sheet_name='Sheet2')

writer = pd.ExcelWriter('written_with_pandas.xlsx')
# df.to_excel(writer, sheet_name='Sheet1', startrow=10, startcol=1)
# df.to_excel(writer, sheet_name='Sheet2')
# writer.save()

depts = ['afrs', 'ASL', 'Chin']

for dept in depts:
        df.to_excel(writer, sheet_name=dept, startrow=10, startcol=1)
writer.save()

a = np.arange(5)
w = pd.ExcelWriter('e.xlsx')
df_list = []
for i in a:
        df = pd.DataFrame({'a':np.random.randint(1, 100, 10)})
        df_list.append(df)
for i, df in enumerate(df_list):
        df.to_excel(w, sheet_name=f'sheet{i}')
w.save()