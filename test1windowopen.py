import graphics as g
from graphics import *
import numpy as np
import pandas as pd

win = g.GraphWin('pivot table test', 1000, 500)


def data1():
    data = {'A':['foo','foo','foo','bar','bar','bar'],
            'B':['one','one','two','two','one','one'],
            'C':['x','y','x','y','x','y'],
            'D':[1,3,2,5,4,1]}
    df = pd.DataFrame(data)
    df.pivot_table(values='D',index=['A','B'],columns=['C'])
    return data1

def main():
    data1()
    win.getMouse()
    win.setBackground( 'black' )
    win.getMouse()
    win.close()
    
main()