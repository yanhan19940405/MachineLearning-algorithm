import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data=pd.DataFrame({1:[1,'S',-1],
                   2:[1,'M',-1],
                   3:[1,'M',1],
                   4:[1,'S',1],
                   5:[1,'S',-1],
                   6:[2,'S',-1],
                   7:[2,'M',-1],
                   8:[2,'M',1],
                   9:[2,'L',1],
                   10:[2,'L',1],
                   11:[3,'L',1],
                   12:[3,'M',1],
                   13:[3,'M',1],
                   14:[3,'L',1],
                   15:[3,'L',-1]},index=['X1','X2','Y'])
print(data.iloc[0:2,:])
data2=list(data.iloc[2,:])
data3=list(data.iloc[0,:])
data4=list(data.iloc[1,:])
def I(v):
    if v>0:
        return 1
    else:
        return -1

def p(N,Y):
    sum = 0
    for i in data2:
        if(i==Y):
            sum = sum + I(i)
    return abs(sum)/N
def I2(X,Y,N):
    a=0
    b=0
    n=0
    A1=np.array([1,2,3],dtype=np.int)
    A2=np.array(['S','M','L'],dtype=np.str)
    Y1=[-1,1]
    if X in A1:
        while n < len(data2):
            if X==data3[n] and Y ==data2[n]:
                a=a+1
            n = n + 1
        return a/(N*p(N,Y))
    elif X in A2:
        while n < len(data2):
            if X==data4[n] and Y ==data2[n]:
                b=b+1
            n = n + 1
        return b/(N*p(N,Y))

if __name__=='__main__':
#数据分类X.T=[3,S]
    X=[3,"S"]
    W=float(p(15,1)*I2(X[1],1,15)*I2(X[0],1,15))
    M=float(p(15,-1)*I2(X[1],-1,15)*I2(X[0],-1,15))
    if W>M:
        print("数据X分类属于Y=1")
    elif W<M:
        print("数据X分类属于Y=-1")
    else:
        print("数据X分类属于同类")
