# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:47:57 2021

@author: xuhaoyan
"""

import numpy as np
from pandas import Series, DataFrame


#Action1：求2+4+6+8+...+100的求和
def work1():
    X1=np.arange(2,102,2)
    print(sum(X1))

#Action2: 统计全班的成绩
def work2():
    data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
    df1 = DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'])
    print(df1.describe())
    print(df1.var())
    
    df1['Score']=df1.apply(lambda x: x.sum(),axis=1)
    df1 = df1.sort_values('Score',ascending=False).reset_index()
    print(df1)

#Action3: 对汽车质量数据进行统计
def work3():
    import pandas as pd
    df = pd.read_csv('./car_complain.csv')
    df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))

    def f(x):
        x = x.replace('一汽-大众','一汽大众')
        return x
    df['brand'] = df['brand'].apply(f)
    #数据统计
    #①品牌投诉总数
    result1 = df.groupby(['brand'])['id'].agg(['count'])
    result1 = result1.sort_values('count',ascending=False)
    print(result1)
    #车型投诉总数
    result2 = df.groupby(['car_model'])['id'].agg(['count'])
    result2 = result2.sort_values('count',ascending=False)
    print(result2)
    #哪个品牌的平均车型投诉最多
    result3 = df.groupby(['brand','car_model'])['id'].agg(['count'])
    result3 = result3.sort_values('count',ascending=False)
    print(result3)

#work1()
#work2()
work3()