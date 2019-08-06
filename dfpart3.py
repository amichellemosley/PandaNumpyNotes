import numpy as np
import pandas as pd
from numpy.random import randn
#index levels

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

#output: [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

df = pd.DataFrame(randn(6,2,),hier_index,['A','B'])

df.loc['G1']

df.index.names = ['Groups','Num']

df.loc['G2'].loc[2]['B']

#output 0.627549094912734
#remember df =
#                   A         B
#Groups Num                    
#G1     1    0.716979 -0.299423
 #      2   -0.108891 -0.316806
  #     3    0.427692  0.078198
#G2     1   -1.011023 -0.787498
#       2    0.722617  0.627549
 #      3    1.470223 -0.571811
 
df.xs('G1')
 
 #xs is the group loc is the smaller groupes in the group

df.xs(1,level='Num')

