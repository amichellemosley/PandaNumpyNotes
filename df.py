#DATAFRAMES PART 2

import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# run df > 0 returns boolan values


#df[df['Z']<0]

resultdf = df[df['W']>0]

df[(df['W']> 0) & (df['Y']> 1)] #don't do and do & or raise error ambigious 

# | = or

df.reset_index()
newind = 'CA NY WY OR CO'.split()
#output ['CA', 'NY', 'WY', 'OR', 'CO']


df['States'] = newind

df.set_index('States')



