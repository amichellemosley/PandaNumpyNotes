#NumPY Indexing

import numpy as np

arr = np.arrange(0,11)
#output 0-10

arr[8]
#output 8

arr[1:5]
#output 1-4 not 5 or 0

arr[0:5]

arr[:6]
#output 0-5

arr[5:]
#output 5-10, because orginal arr was 0-10

arr[0:5] = 100
#output would give you 5 100's, and 5-10

sliecofarr = arr[0:6]
sliceofarr[:] = 99
#output will be 6 99's

arrcopy = arr.copy()
#output 6 99's and 6-10

arr2d = np.array ([[5,10,15],[20,25,30],[35,40,45]])

arr2d[0][0] #oupt will be 5

arr2d[1][1] #output is 25

arr > 5 #output boolan values for greater than 5

boolarr = aa > 5
arr[boolarr]

arr2d = np.arange(5).reshape(5,10)


