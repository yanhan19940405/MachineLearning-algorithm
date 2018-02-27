
import random
import numpy as np
import matplotlib.pyplot as plt


def sign(v):
    if v>=0:
        return 1
    else:
        return -1

def train(num,datas,lr):
    w=0.0
    b=0
    datas_len = len(datas)
    alpha = [0 for i in range(datas_len)]
    array = np.array(datas)
    gram = np.matmul(array[:,0:-1] ,array[:,0:-1].T)
    for idx in range(num):
        tmp=0
        i = random.randint(0,datas_len-1)
        yi=array[i,-1]
        for j in range(datas_len):
            tmp+=alpha[j]*array[j,-1]*gram[i,j]
        tmp+=b
        if(yi*tmp<=0):
            alpha[i]=alpha[i]+lr
            b=b+lr*yi
    for i in range(datas_len):
        w+=alpha[i]*array[i,0:-1]*array[i,-1]
    return w,b,alpha,gram
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
    datas = data1 + data2+data3  # 样本集
    w, b, alpha, gram = train(num=500, datas=datas, lr=0.01)
    points(datas,w,b)