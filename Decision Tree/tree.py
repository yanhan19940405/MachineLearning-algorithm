import pandas as pd
import math
import matplotlib.pyplot as plt  # 载入 pyplot API

data= pd.read_table("tree.txt", header=None, encoding='utf-8', delim_whitespace=True)
sizex=data.iloc[:,0].size
sizey=data.iloc[0,:].size-1
def H(data):#计算数据D中经验熵
    h = []
    for i in data.iloc[:,sizey].values:
        h.append(i)
    l=list(set(h))
    K=len(l)##经验熵中K值
    D=len(h)
    class1=0
    class2=0
    for j in h:
        if j=="是":
            class1=class1+1
        elif j=="否":
            class2=class2+1
    H=-((class1/D)*(math.log2((class1/D))))-((class2/D)*(math.log2((class2/D))))
    return H
def g1(data,sizex):#计算数据D中feature1条件熵
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
        if j1=="青年":
            class3=class3+1
        elif j1=="老年":
            class4=class4+1
        elif j1 == "中年":
            class5=class5+1
    H1=-((2/class3)*(math.log2((2/class3))))-((3/class3)*(math.log2((3/class3))))
    H2 = -((2 / class4) * (math.log2((2 / class4)))) - ((3 / class4) * (math.log2((3 / class4))))
    H3 = -((1 / class5) * (math.log2((1/ class5)))) - ((4/ class5) * (math.log2((4/ class5))))
    print(class3)
    print(class4)
    print(class5)
    g1=H(data)-(class3/sizex)*H1-(class4/sizex)*H2-(class5/sizex)*H3
    return g1
def g2(data,sizex):#计算数据D中feature2条件熵
    v1=[]
    for u1 in data.iloc[:, 1].values:
        v1.append(u1)
    l1= list(set(v1))
    print(l1)
    K=len(l1)
    class6 = 0
    class7 = 0
    for j1 in v1:
        if j1=="否":
            class6=class6+1
        elif j1=="是":
            class7=class7+1

    H1=0
    H2 = -((4/ class6) * (math.log2((4/ class6)))) - ((6 / class6) * (math.log2((6/ class6))))
    print(class6)
    print(class7)
    g2=H(data)-(class7/sizex)*H1-(class6/sizex)*H2
    return g2
def g3(data,sizex):#计算数据D中feature3条件熵
    v1=[]
    for u1 in data.iloc[:, 2].values:
        v1.append(u1)
    l1= list(set(v1))
    print(l1)
    K=len(l1)
    class8 = 0
    class9 = 0
    for j1 in v1:
        if j1=="否":
            class8=class8+1
        elif j1=="是":
            class9=class9+1

    H1=0
    H2 = -((3/ class8) * (math.log2((3/ class8)))) - ((6 / class8) * (math.log2((6/ class8))))
    print(class8)
    print(class9)
    g3=H(data)-(class9/sizex)*H1-(class8/sizex)*H2
    return g3
def g4(data,sizex):#计算数据D中feature4条件熵
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
        if j1=="一般":
            class10=class10+1
        elif j1=="好":
            class11=class11+1
        elif j1=="非常好":
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
    print("该决策树根节点为第三个特征的节点即为g3函数的节点值")
    ##tree={"column":list(data.columns)[3],"left":{"label":}}
    tree["feature3"]={}
    m=[a for a,x in enumerate(list(data.iloc[:,2])) if x=="是"]
    n=[a for a,x in enumerate(list(data.iloc[:,2])) if x=="否"]
    for i in n:
        g.append(list(data.iloc[:,4])[i])
    for l in m:
        w.append(list(data.iloc[:,4])[l])
    print(w)
    print(g)
    if len(list(set(w)))==1 and len(list(set(g))) !=1:#此处根据叶节点取得值判断同时所取的分类数据构成所在list的重复元素长读,若为1则表示叶节点都为同一类数据
        g1_second=0.251
        g2_second = 0.918
        g4_second=0.474
        treenodes_second = [g1_second,g2_second,g4_second]
        treew_second = sorted(treenodes_second, reverse=True)
        print(treew_second)
        print("该决策树下一个中心结点为第二个特征的节点即为feature2")
        tree["feature3"]["是"]={"id":0,"value":'是'}
        tree["feature3"]["否"]={}
        m1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "是"]
        n1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "否"]
        for i in n1:
            go.append(list(data.iloc[:, 4])[i])
        for l in m1:
            w1.append(list(data.iloc[:, 4])[l])
        print("根节点左侧为同一类则为叶子节点,右侧则为非同一类型值则为中心节点")
        #在第一个根节点右侧取否的情况下再次判定第二个中心顶点分支情况，若叶节点取值全部为同一类则决策树生成完毕
        G=m1+m##取交集
        W=n+n1##取交集
        w2 =[x for x in W if W.count(x) == 2]##根据列表中数据个数筛选
        G2=[x for x in G if G.count(x) == 2]##根据列表中数据个数筛选
        print("w",W)

        for i1 in w2:
            go2.append(list(data.iloc[:, 4])[i1])
        for l1 in G2:
            w3.append(list(data.iloc[:, 4])[l1])
        if len(list(set(w3)))==1 and len(list(set(go2))) ==1:
            tree["feature3"]["否"]["feature2"]={}
            tree["feature3"]["否"]["feature2"]["是"]={"id":1,"value":'是'}
            tree["feature3"]["否"]["feature2"]["否"] = {"id": 2, "value": '否'}
    return tree
def prediction(X,classify):#根据决策树的预测函数
    if X[2]=="是":
        return str(X)+"分类属于" + ""+classify[0]+""+"这一类"
    elif X[2]=="否":
        if X[1]=="是":
            return str(X)+"分类属于"+ ""+classify[0]+""+"这一类"
        elif X[1]=="否":
            return str(X)+"分类属于" + ""+ classify[1]+""+"这一类"





if __name__=='__main__':
    X1=["老年","是","否","一般"]
    X2 = ["青年", "否", "是", "一般"]
    X3 = ["老年", "否", "否", "好"]
    classifynum=['是', '否']
    tree=data
    print('决策树',create_tree(tree))
    print(prediction(X1, classifynum))
    print(prediction(X2, classifynum))
    print(prediction(X3, classifynum))


