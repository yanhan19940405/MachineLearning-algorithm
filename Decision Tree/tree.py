import pandas as pd
import math
import matplotlib.pyplot as plt  # ���� pyplot API

data= pd.read_table("tree.txt", header=None, encoding='utf-8', delim_whitespace=True)
sizex=data.iloc[:,0].size
sizey=data.iloc[0,:].size-1
def H(data):#��������D�о�����
    h = []
    for i in data.iloc[:,sizey].values:
        h.append(i)
    l=list(set(h))
    K=len(l)##��������Kֵ
    D=len(h)
    class1=0
    class2=0
    for j in h:
        if j=="��":
            class1=class1+1
        elif j=="��":
            class2=class2+1
    H=-((class1/D)*(math.log2((class1/D))))-((class2/D)*(math.log2((class2/D))))
    return H
def g1(data,sizex):#��������D��feature1������
    v=[]
    for u in data.iloc[:, 0].values:
        v.append(u)
    l1= list(set(v))
    print(l1)
    K=len(l1)
    class3 = 0
    class4 = 0
    class5=0
    for j1 in v:
        if j1=="����":
            class3=class3+1
        elif j1=="����":
            class4=class4+1
        elif j1 == "����":
            class5=class5+1
    H1=-((2/class3)*(math.log2((2/class3))))-((3/class3)*(math.log2((3/class3))))
    H2 = -((2 / class4) * (math.log2((2 / class4)))) - ((3 / class4) * (math.log2((3 / class4))))
    H3 = -((1 / class5) * (math.log2((1/ class5)))) - ((4/ class5) * (math.log2((4/ class5))))
    print(class3)
    print(class4)
    print(class5)
    g1=H(data)-(class3/sizex)*H1-(class4/sizex)*H2-(class5/sizex)*H3
    return g1
def g2(data,sizex):#��������D��feature2������
    v1=[]
    for u1 in data.iloc[:, 1].values:
        v1.append(u1)
    l1= list(set(v1))
    print(l1)
    K=len(l1)
    class6 = 0
    class7 = 0
    for j1 in v1:
        if j1=="��":
            class6=class6+1
        elif j1=="��":
            class7=class7+1

    H1=0
    H2 = -((4/ class6) * (math.log2((4/ class6)))) - ((6 / class6) * (math.log2((6/ class6))))
    print(class6)
    print(class7)
    g2=H(data)-(class7/sizex)*H1-(class6/sizex)*H2
    return g2
def g3(data,sizex):#��������D��feature3������
    v1=[]
    for u1 in data.iloc[:, 2].values:
        v1.append(u1)
    l1= list(set(v1))
    print(l1)
    K=len(l1)
    class8 = 0
    class9 = 0
    for j1 in v1:
        if j1=="��":
            class8=class8+1
        elif j1=="��":
            class9=class9+1

    H1=0
    H2 = -((3/ class8) * (math.log2((3/ class8)))) - ((6 / class8) * (math.log2((6/ class8))))
    print(class8)
    print(class9)
    g3=H(data)-(class9/sizex)*H1-(class8/sizex)*H2
    return g3
def g4(data,sizex):#��������D��feature4������
    v1=[]
    for u1 in data.iloc[:, 3].values:
        v1.append(u1)
    l1= list(set(v1))
    print(l1)
    K=len(l1)
    class10 = 0
    class11 = 0
    class12=0
    for j1 in v1:
        if j1=="һ��":
            class10=class10+1
        elif j1=="��":
            class11=class11+1
        elif j1=="�ǳ���":
            class12=class12+1

    H1=-((1/ class10) * (math.log2((1/ class10)))) - ((4/ class10) * (math.log2((4/ class10))))
    H2 = -((2/ class11) * (math.log2((2/ class11)))) - ((4 / class11) * (math.log2((4/ class11))))
    H3 = 0
    g4=H(data)-(class10/sizex)*H1-(class11/sizex)*H2-(class12/sizex)*H3
    return g4
def create_tree(data):
    g=[]
    w=[]
    go=[]
    w1=[]
    go2 = []
    w3 = []
    j=0
    k=0
    tree={}
    treenodes=[float(g1(data,sizex)),float(g2(data,sizex)),float(g3(data,sizex)),float(g4(data,sizex))]
    treew=sorted(treenodes,reverse=True)
    print(treew)
    print("�þ��������ڵ�Ϊ�����������Ľڵ㼴Ϊg3�����Ľڵ�ֵ")
    ##tree={"column":list(data.columns)[3],"left":{"label":}}
    tree["feature3"]={}
    m=[a for a,x in enumerate(list(data.iloc[:,2])) if x=="��"]
    n=[a for a,x in enumerate(list(data.iloc[:,2])) if x=="��"]
    for i in n:
        g.append(list(data.iloc[:,4])[i])
    for l in m:
        w.append(list(data.iloc[:,4])[l])
    print(w)
    print(g)
    if len(list(set(w)))==1 and len(list(set(g))) !=1:#�˴�����Ҷ�ڵ�ȡ��ֵ�ж�ͬʱ��ȡ�ķ������ݹ�������list���ظ�Ԫ�س���,��Ϊ1���ʾҶ�ڵ㶼Ϊͬһ������
        g1_second=0.251
        g2_second = 0.918
        g4_second=0.474
        treenodes_second = [g1_second,g2_second,g4_second]
        treew_second = sorted(treenodes_second, reverse=True)
        print(treew_second)
        print("�þ�������һ�����Ľ��Ϊ�ڶ��������Ľڵ㼴Ϊfeature2")
        tree["feature3"]["��"]={"id":0,"value":'��'}
        tree["feature3"]["��"]={}
        m1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "��"]
        n1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "��"]
        for i in n1:
            go.append(list(data.iloc[:, 4])[i])
        for l in m1:
            w1.append(list(data.iloc[:, 4])[l])
        print("���ڵ����Ϊͬһ����ΪҶ�ӽڵ�,�Ҳ���Ϊ��ͬһ����ֵ��Ϊ���Ľڵ�")
        #�ڵ�һ�����ڵ��Ҳ�ȡ���������ٴ��ж��ڶ������Ķ����֧�������Ҷ�ڵ�ȡֵȫ��Ϊͬһ����������������
        G=m1+m##ȡ����
        W=n+n1##ȡ����
        w2 =[x for x in W if W.count(x) == 2]##�����б������ݸ���ɸѡ
        G2=[x for x in G if G.count(x) == 2]##�����б������ݸ���ɸѡ
        print("w",W)

        for i1 in w2:
            go2.append(list(data.iloc[:, 4])[i1])
        for l1 in G2:
            w3.append(list(data.iloc[:, 4])[l1])
        if len(list(set(w3)))==1 and len(list(set(go2))) ==1:
            tree["feature3"]["��"]["feature2"]={}
            tree["feature3"]["��"]["feature2"]["��"]={"id":1,"value":'��'}
            tree["feature3"]["��"]["feature2"]["��"] = {"id": 2, "value": '��'}
    return tree
def prediction(X,classify):#���ݾ�������Ԥ�⺯��
    if X[2]=="��":
        return str(X)+"��������" + ""+classify[0]+""+"��һ��"
    elif X[2]=="��":
        if X[1]=="��":
            return str(X)+"��������"+ ""+classify[0]+""+"��һ��"
        elif X[1]=="��":
            return str(X)+"��������" + ""+ classify[1]+""+"��һ��"





if __name__=='__main__':
    X1=["����","��","��","һ��"]
    X2 = ["����", "��", "��", "һ��"]
    X3 = ["����", "��", "��", "��"]
    classifynum=['��', '��']
    tree=data
    print('������',create_tree(tree))
    print(prediction(X1, classifynum))
    print(prediction(X2, classifynum))
    print(prediction(X3, classifynum))


