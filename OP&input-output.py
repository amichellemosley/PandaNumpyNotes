import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
                        
df['col2'].unique()
df['col2'].value_counts()
df[df['col1']>2] #will return boolan
df[(df['col1']>2) & (df['col1']==444)]

def times2(x):
    return x*2
df['col1'].apply(times2)

df['col3'].apply(lambda x: x*2)
df.drop('col1',axis=1)
df.columns
df.index
df.sort_values(by='col2')
df.isnull() #returns false boolan

#While making a Data Frame from a csv file, many blank columns are
#imported as null value into the Data Frame which later creates problems
#while operating that data frame. Pandas isnull() and notnull() methods are
#used to check and manage NULL values in a data frame.

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df.pivot_table(values='D',index=['A','B'],columns=['C'])

# with pip install sqlalchemy, lxml, html5lib, BeautifulSoup4

#pwd output: 'C:\\Users\\Marcial'
#pd.read_csv('example.csv')

#df = pd.read_csv('example.csv')
#df.to_csv('My_Output', index=False)
#pd.read_csv('My_output')



pd.read_excel('Excel_Sample.xlsx', sheetname='Sheet1')

df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')
data = pd.read_html('link here.com')

type(data) #output: list
data[0].head()


from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)

sqldf = pd.read_sql('my_table',con=engine)
sqldf