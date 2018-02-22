import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
X=[67,32000,0.1]
data = pd.read_table('1.txt',header=None,encoding='gb2312',delim_whitespace=True)
data2=data
print(len(data))
print(data.values)
maxdata=max(data.max())
mindata=min(data.min())
x1=[(X[0]-mindata)/(maxdata-mindata),(X[1]-mindata)/(maxdata-mindata),(X[2]-mindata)/(maxdata-mindata)]
print("x1",x1)
n=data.columns.size-1
k=5
print("n",n)
m=0
##按照行或者列遍历进行数据归一化处理
while m<data.iloc[:,0].size :
    data.iloc[m,:n]=(data.iloc[m,:n]-mindata)/(maxdata-mindata)
    m = m + 1
print(data)
u=0
l=[]
j=len(l)
while u<data.iloc[:,0].size :
    v1=np.square(data.iloc[u,0]-x1[0])
    v2=np.square(data.iloc[u,1]-x1[1])
    v3=np.square(data.iloc[u,2]-x1[2])
    l.append(np.sqrt(v1+v2+v3))
    u=u+1
    j=j+1

t=pd.DataFrame(l,columns=['a'])
t['answer']=data.iloc[:,3]
print(t)
p=t.sort_values(by=["a"])

print(p)
print("特征向量X分类属于：",p.iloc[:k,1])
ax=p.plot.scatter(y="a",x="answer",color="blue",label="class1")
p[0:k].plot.scatter(y="a",x="answer",color="red",label="class2",ax=ax)
plt.show()