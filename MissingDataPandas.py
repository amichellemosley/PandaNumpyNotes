import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df.dropna(axis=1)


df.fillna(value='Fill Value')

df['A'].fillna(value=df['A'].mean())



#Groupby allows you to group together rows based off of a column and perform
#an aggregate function on them

data = {'Company' :['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)

df.groupby('Company')
#output: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x045C3B70>

byComp = df.groupby('Company')

byComp.mean()
#output: 
#         Sales
#Company       
#FB       296.5
#GOOG     160.0
#MSFT     232.0

byComp.sum()
byComp.std()
byComp.sum().loc['FB']

df.groupby('Company').min()
df.groupby('Company').describe()
df.groupby('Company').describe().transpose()['FB']



df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['AB', 'A9', 'A10', 'A11'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8,9,10,11])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8,9,10,11])
                   
                   

#to concate
#pd.concat([df1,df2,df3])

