import pandas as pd
import numpy as np
import math
data= pd.read_table("tree.txt", header=None, encoding='utf-8', delim_whitespace=True)
sizey=data.iloc[:,0].size
sizex=data.iloc[0,:].size-1
g = []
w = []
go = []
w1 = []
go2 = []
w3 = []
j = 0
k = 0
tree = {}
print(data)
print(sizex)
print(sizey)
def Mount(i,value,value1,value2):
    value=str(value)
    value1=str(value1)
    value2=str(value2)
    i=int(i)
    j=0
    l=0
    M=0
    t1=0
    t2=0
    t3 =0
    t4=0
    t5=0
    t6=0
    t7=0
    t8=0
    t9=0
    e1 = [a for a, x in enumerate(list(data.iloc[:, i])) if x == value]
    e2 = [a for a, x in enumerate(list(data.iloc[:, i])) if x == value1]
    e3 = [a for a, x in enumerate(list(data.iloc[:, i])) if x == value2]
    print(e1)
    print(e2)
    print(e3)
    for k in data.iloc[:,i].values:
        if k ==value:
            if (data.iloc[:, 4].values)[e1[t1]]=="是":
                t2=t2+1
            elif (data.iloc[:, 4].values)[e1[t1]]=="否":
                t3=t3+1
            j=j+1
            t1=t1+1
        elif k==value1:
            if (data.iloc[:, 4].values)[e2[t4]]=="是":
                t5=t5+1
            elif (data.iloc[:, 4].values)[e2[t4]]=="否":
                t6=t6+1
            l=l+1
            t4 = t4 + 1
        elif k==value2:
            if (data.iloc[:, 4].values)[e3[t7]]=="是":
                t8=t8+1
            elif (data.iloc[:, 4].values)[e3[t7]]=="否":
                t9=t9+1
            M=M+1
            t7=t7+1
    return j,l,M,t2,t3,t5,t6,t8,t9
def Gini(i,value,value1,value2,feature,j,l,M,t2,t3,t5,t6,t8,t9):
    v=[]
    if feature=="feature1":
        Gini1=round((j/sizey)*(2*(t2/j)*(t3/j))+(1-(j/sizey))*(2*((t5+t8)/(l+M))*((t6+t9)/(l+M))),2)
        Gini2 = round((l / sizey) * (2 * (t5 / l) * (t6 / l)) + (1 - (l/ sizey)) * (2 * ((t2 + t8) / (j + M)) * ((t3 + t9) / (j + M))),2)
        Gini3 = round((M / sizey) * (2 * (t8 / M) * (t9 / M)) + (1 - (M / sizey)) * (2 * ((t2 + t5) / (j + l)) * ((t3 + t6) / (l + j))),2)
        v.extend([Gini1,Gini2,Gini3])
    elif feature=="feature2":
        Gini4 = round((j / sizey) * (2 * (t2 / j) * (t3 / j)) + (1 - (j / sizey)) * (
                2 * ((t5 + t8) / (l + M)) * ((t6 + t9) / (l + M))),2)
        Gini5 = round((l / sizey) * (2 * (t5 / l) * (t6 / l)) + (1 - (l / sizey)) * (
                2 * ((t2 + t8) / (j + M)) * ((t3 + t9) / (j + M))),2)
        v.extend([Gini4, Gini5])
    elif feature=="feature3":
        Gini7 = round((j / sizey) * (2 * (t2 / j) * (t3 / j)) + (1 - (j / sizey)) * (
                2 * ((t5 + t8) / (l + M)) * ((t6 + t9) / (l + M))),2)
        Gini8 = round((l / sizey) * (2 * (t5 / l) * (t6 / l)) + (1 - (l / sizey)) * (
                2 * ((t2 + t8) / (j + M)) * ((t3 + t9) / (j + M))),2)
        v.extend([Gini7, Gini8])
    elif feature=="feature4":
        Gini10 = round((j / sizey) * (2 * (t2 / j) * (t3 / j)) + (1 - (j / sizey)) * (
                2 * ((t5 + t8) / (l + M)) * ((t6 + t9) / (l + M))),2)
        Gini11 = round((l / sizey) * (2 * (t5 / l) * (t6 / l)) + (1 - (l / sizey)) * (
                2 * ((t2 + t8) / (j + M)) * ((t3 + t9) / (j + M))),2)
        Gini12= round((M / sizey) * (2 * (t8 / M) * (t9 / M)) + (1 - (M / sizey)) * (
                2 * ((t2 + t5) / (j + l)) * ((t3 + t6) / (l + j))),2)
        v.extend([Gini10, Gini11, Gini12])
    return v
def Gini_scecond(feature,t2,t3,t5,t6,t8,t9):
    Gini_scecond_list=[]
    m3 = [a for a, x in enumerate(list(data.iloc[:, 2])) if x == "否"]
    m1 = [a for a, x in enumerate(list(data.iloc[:, 0])) if x == "青年"]
    m11 = [a for a, x in enumerate(list(data.iloc[:, 0])) if x == "中年"]
    m12 = [a for a, x in enumerate(list(data.iloc[:, 0])) if x == "老年"]
    m2 = [a for a, x in enumerate(list(data.iloc[:, 1])) if x == "否"]
    m21 = [a for a, x in enumerate(list(data.iloc[:, 1])) if x == "是"]
    m4 = [a for a, x in enumerate(list(data.iloc[:, 3])) if x == "一般"]
    m41 = [a for a, x in enumerate(list(data.iloc[:, 3])) if x == "好"]
    m42 = [a for a, x in enumerate(list(data.iloc[:, 3])) if x == "非常好"]
    g1 = m1 + m3
    g2 = m3 + m11
    g3 = m3 + m12
    g4 = m3 + m2
    g5 = m3 + m21
    g6 = m3 + m4
    g7 = m3 + m41
    g8 = m3 + m42
    w1 = [x for x in g1 if g1.count(x) == 2]
    w2 = [x for x in g2 if g2.count(x) == 2]
    w3 = [x for x in g3 if g3.count(x) == 2]
    w4 = [x for x in g4 if g4.count(x) == 2]
    w5 = [x for x in g5 if g5.count(x) == 2]
    w6 = [x for x in g6 if g6.count(x) == 2]
    w7 = [x for x in g7 if g7.count(x) == 2]
    w8 = [x for x in g8 if g8.count(x) == 2]
    print("g1",g1)
    print("m3", m3)
    print("w2", w2)
    print("w3", w3)
    print("w4", w4)
    print("w5", w5)
    print("w6", w6)
    print("w7", w7)
    print("w8", w8)
    if feature=="feature1":
        Gini_second_feature1 = (len(w1)/2 / len(m3)) * (2*(t2/len(w1)/2)*(t3/len(w1)/2))+(1-(len(w1)/2 / len(m3)))*(2*((t5+t8)/(len(m3)-len(w1)/2))*((t6+t9)/(len(m3)-len(w1)/2)))
        Gini_second_feature1_2 = (len(w2)/2 / len(m3)) * (2 * (t5 / len(w2)/2) * (t6 / len(w2)/2)) + (1 - (len(w2)/2 / len(m3))) * (
            2 * ((t2 + t8) / (len(m3) - len(w2)/2)) * ((t3 + t9) / (len(m3) - len(w2)/2)))
        Gini_second_feature1_3 = (len(w3)/2 / len(m3)) * (2 * (t8 / len(w3)/2) * (t9 / len(w3)/2)) + (1 - (len(w3) / len(m3)/2)) * (
            2 * ((t2 + t5) / (len(m3) - len(w3)/2)) * ((t3 + t6) / (len(m3) - len(w3)/2)))
        Gini_scecond_list.extend([Gini_second_feature1,Gini_second_feature1_2,Gini_second_feature1_3 ])
    elif feature=="feature2":
        Gini_second_feature2 = (len(w4)/2 / len(m3)) * (2 * (t6 / len(w4)/2) * (1-(t6 / len(w4)/2))) +(len(w5)/2 / len(m3)) * (2 * (t5 / len(w5)/2) * (1-(t5 / len(w4)/2)))
        Gini_second_feature2_1 = (len(w5)/2 / len(m3)) * (2 * (t5 / len(w5)/2) * (1-(t5 / len(w4)/2))) + (len(w4)/2 / len(m3)) * (2 * (t6 / len(w4)/2) * (1-(t6 / len(w4)/2)))
        Gini_scecond_list.extend([Gini_second_feature2, Gini_second_feature2_1])
    elif feature == "feature4":
        Gini_second_feature4 = (len(w6)/2 / len(m3)) * (2 * (t2 / len(w6)/2) * (t3 / len(w6)/2)) + (1 - (len(w6)/2 / len(m3))) * (
            2 * ((t5 + t8) / (len(m3) - len(w6)/2)) * ((t6 + t9) / (len(m3) - len(w6)/2)))
        Gini_second_feature4_1 = (len(w7)/2 / len(m3)) * (2 * (t5 / len(w7)/2) * (t6 / len(w7)/2)) + (1 - (len(w7)/2 / len(m3))) * (
            2 * ((t2 + t8) / (len(m3) - len(w7)/2)) * ((t3 + t9) / (len(m3) - len(w7)/2)))
        Gini_second_feature4_2 = (len(w8)/2 / len(m3)) * (2 * (t8 / len(w8)/2) * (t9 / len(w8)/2)) + (1 - (len(w8)/2 / len(m3))) * (
            2 * ((t5 + t2) / (len(m3) - len(w8)/2)) * ((t6 + t3) / (len(m3) - len(w8)/2)))
        Gini_scecond_list.extend([Gini_second_feature4, Gini_second_feature4_1, Gini_second_feature4_2])
        #Gini_scecond_list=[Gini_second_feature1,Gini_second_feature1_2,Gini_second_feature1_3,Gini_second_feature2,Gini_second_feature2_1,Gini_second_feature4,Gini_second_feature4_1,Gini_second_feature4_2]
    return Gini_scecond_list
def prediction(X,classify):#根据决策树的预测函数
    if X[2]=="是":
        return str(X)+"分类属于" + ""+classify[0]+""+"这一类"
    elif X[2]=="否":
        if X[1]=="是":
            return str(X)+"分类属于"+ ""+classify[0]+""+"这一类"
        elif X[1]=="否":
            return str(X)+"分类属于" + ""+ classify[1]+""+"这一类"

if __name__=='__main__':
    print("feature1",Mount(0, "青年", "中年", "老年"))
    print("feature1",Gini(0,"青年", "中年", "老年","feature1",5, 5, 5, 2, 3, 3, 2, 4, 1))
    print("feature2",Mount(1, "是", "否", ""))
    print("feature2", Gini(1, "是", "否", "", "feature2", 5, 10, 0, 5, 0, 4, 6, 0, 0))
    print("feature3",Mount(2, "是", "否", ""))
    print("feature3", Gini(1, "是", "否", "", "feature3", 6, 9, 0, 6, 0, 3, 6, 0, 0))
    print("feature4",Mount(3, "好", "一般", "非常好"))
    print("feature4", Gini(1, "是", "否", "", "feature4", 6, 5, 4, 4, 2, 1, 4, 4, 0))
    v1=Gini(0,"青年", "中年", "老年","feature1",5, 5, 5, 2, 3, 3, 2, 4, 1)+Gini(1, "是", "否", "", "feature2", 5, 10, 0, 5, 0, 4, 6, 0, 0)+ Gini(1, "是", "否", "", "feature3", 6, 9, 0, 6, 0, 3, 6, 0, 0)+Gini(1, "是", "否", "", "feature4", 6, 5, 4, 4, 2, 1, 4, 4, 0)
    print(v1)
    treew = sorted(v1, reverse=True)
    print("该决策树根节点为第三个特征的节点即为g3函数的节点值")
    ##tree={"column":list(data.columns)[3],"left":{"label":}}
    tree["feature3"] = {}
    m = [a for a, x in enumerate(list(data.iloc[:, 2])) if x == "是"]
    print("m", m)
    n = [a for a, x in enumerate(list(data.iloc[:, 2])) if x == "否"]
    for i in n:
        g.append(list(data.iloc[:, 4])[i])
    for l in m:
        w.append(list(data.iloc[:, 4])[l])
    print(w)
    print(g)
    if len(list(set(w))) == 1 and len(list(set(g))) != 1:  # 此处根据叶节点取得值判断同时所取的分类数据构成所在list的重复元素长读,若为1则表示叶节点都为同一类数据

        print("feature1",Gini_scecond("feature1", 2, 3, 3, 2, 4, 1))
        print("feature2", Gini_scecond("feature2", 5, 0, 4, 6, 0, 0))
        print("feature4", Gini_scecond("feature4", 4, 2, 1, 4, 4, 0))
        #t2,t3,t5,t6,t8,t9)
        v2=[Gini_scecond("feature1", 2, 3, 3, 2, 4, 1),Gini_scecond("feature2", 5, 0, 4, 6, 0, 0),Gini_scecond("feature4", 4, 2, 1, 4, 4, 0)]
        treew1 = sorted(v2, reverse=False)
        print("第二次GINI值排列顺序",treew1)
        print("该决策树下一个中心结点为第二个特征的节点即为feature2")
        tree["feature3"]["是"] = {"id": 0, "value": '是'}
        tree["feature3"]["否"] = {}
        m1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "是"]
        n1 = [a1 for a1, x in enumerate(list(data.iloc[:, 1])) if x == "否"]
        for i in n1:
            go.append(list(data.iloc[:, 4])[i])
        for l in m1:
            w1.append(list(data.iloc[:, 4])[l])
        print("根节点左侧为同一类则为叶子节点,右侧则为非同一类型值则为中心节点")
        # 在第一个根节点右侧取否的情况下再次判定第二个中心顶点分支情况，若叶节点取值全部为同一类则决策树生成完毕
        G = m1 + m  ##取交集
        W = n + n1  ##取交集
        w2 = [x for x in W if W.count(x) == 2]  ##根据列表中数据个数筛选
        G2 = [x for x in G if G.count(x) == 2]  ##根据列表中数据个数筛选
        print("w", W)

        for i1 in w2:
            go2.append(list(data.iloc[:, 4])[i1])
        for l1 in G2:
            w3.append(list(data.iloc[:, 4])[l1])
        if len(list(set(w3))) == 1 and len(list(set(go2))) == 1:
            tree["feature3"]["否"]["feature2"] = {}
            tree["feature3"]["否"]["feature2"]["是"] = {"id": 1, "value": '是'}
            tree["feature3"]["否"]["feature2"]["否"] = {"id": 2, "value": '否'}
        print(tree)
    X1 = ["老年", "是", "否", "一般"]

    X2 = ["青年", "否", "是", "一般"]
    X3 = ["老年", "否", "否", "好"]
    classifynum = ['是', '否']
    tree = data
    print(prediction(X1, classifynum))
    print(prediction(X2, classifynum))
    print(prediction(X3, classifynum))
