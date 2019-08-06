#NumPY Arrays

myList = [1,2,3]

import numpy as np
arr = np.array(myList)

myMat = [[1,2,3], [4,5,6], [7,8,9]]

np.array(myMat)

np.arange(0,11, 2)
#output= anything up to 11 by 2's

np.zeros(3)

np.zeros((5,5))
#output= data table array of all zeros 5x5 table

np.ones(4)

np.ones((3,4))
#output 3x4 of all ones

np.linspace(0,5,10)

np.eye(4)


np.random.rand(5)

np.random.rand(5,5)

#output gives you random 5x5 table array

np.random.randint(1,100, 10)
#output is 10 random #'s in table array

ranarr = np.random.randint(0,50,10)

arr.reshape(5,5)

ranarr.argmax()
ranarr.argmin()

ranarr.min()
ranarr.max()

arr = arr.reshape(5,5)
#outputs array table 5x5

arr.shap # outputs (5,5)

arr.dtype #tells you the data type output= dtype('int32')


from numpy.random import randint
randint (2,10)



