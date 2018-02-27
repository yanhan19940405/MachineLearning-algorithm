import random
import numpy as np
import matplotlib.pyplot as plt


def sign(v):
    if v>=0:
        return 1
    else:
        return -1

def train(num,datas,lr):
    w=[0,0]
    b=0
    for i in range(num):
        x=random.choice(datas)
        x1,x2,y=x
        if(y*sign((w[0]*x1+w[1]*x2+b))<=0):
            w[0]+=lr*y*x1
            w[1]+=lr*y*x2
            b+=lr*y
    return w,b
def points(datas,w,b):
    plt.figure()
    x1 = np.linspace(0, 8, 100)
    x2 = (-b-w[0]*x1)/w[1]
    plt.plot(x1, x2, color='r', label='y1 data')
    datas_len=len(datas)
    for i in range(datas_len):
        if(datas[i][-1]==1):
            plt.scatter(datas[i][0],datas[i][1],s=100)
        else:
            plt.scatter(datas[i][0],datas[i][1],marker='x',s=100)
    plt.show()


if __name__=='__main__':
    data1 = [[1, 3, 1], [2, 2, 1], [3, 8, 1], [2, 6, 1],[4,6,1]]
    data2 = [[2, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1],[5,4,-5]]
    data3 = [[5, 1, -6], [8, 1, -2], [5, 3, -1], [7, 6, 0],[6,2,-6]]
    datas = data1 + data2+data3
    w,b=train(num=100,datas=datas,lr=0.1)
    points(datas,w,b)