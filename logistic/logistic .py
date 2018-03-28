import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def change(x):
    return int(x)*1.0
def classify(w,x_test):
    power = np.dot(w, x_test.T)
    result = 1 / (1 + np.exp(-power))
    print("result",result)
    label=[0,1]
    if result>0.5:
        return label[1]
    elif result>0 and result<0.5:
        return label[0]

if __name__=='__main__':
    a = np.loadtxt('testSet.txt',converters={2:change}, usecols=(0, 1)).reshape((100,2))
    b=np.loadtxt('testSet.txt').reshape((100,3))
    print(np.shape(a))
    maxnum=np.max(a)
    minnum=np.min(a)
    a=(a-minnum)/(maxnum-minnum)
    print(np.shape(a[1,0:2].T))
    n=0
    l=[]
    w1=[]
    learn=0.01
    w=np.zeros((100,2))
    w=w*1.00000
    h=np.dot(w,a.T)
#h=w.T.dot(a)
    while  n<100 :
        w=w-learn*(np.dot(np.dot(w[n],(a[n,0:2].T))-b[n,2],a[n,0:2]))
        j=np.square((np.dot(w[n],(a[n,0:2].T))-b[n,2]))
        j1 = (1 / 2) * j
        l.append(j1)
        w1.append(w)
        print(np.abs(w1[n][0, 0] - w1[n - 1][0, 0]) )
        if np.abs(w1[n][0, 0] - w1[n - 1][0, 0])==0  or np.abs(w1[n][0, 1] - w1[n - 1][0, 1])==0:
            if n!=0:
                print("合适的w",w)
                print("合适的n", n)
                w0=w1[n]
        n = n + 1
    print("w0",w0)


    print("合适的W值为:",w0[0])
    #
    x_test=[12.33333343,5.4337643]
    x_test=(x_test-minnum)/(maxnum-minnum)#归一化
    print("x_test",x_test)
    print("数据X分类属于：","第"+str(classify( w[0],x_test))+"类")

