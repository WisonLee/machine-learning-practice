import numpy as np
import pandas as pd

# Series
'''
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
'''
pd.Series([1, 3, 5, np.nan,6,8])

# DataFrame
'''
DatetimeIndex(['2020-02-25', '2020-02-26', '2020-02-27', '2020-02-28',
               '2020-02-29', '2020-03-01', '2020-03-02'],
              dtype='datetime64[ns]', freq='D')
'''
dates = pd.date_range('20200225',periods=7)

'''
                   a         b         c         d
2020-02-25  0.501461 -0.027166  0.686034 -0.591722
2020-02-26 -1.562610 -1.132512 -1.899230 -0.258841
2020-02-27  0.688143 -1.223963  1.546211 -1.394614
2020-02-28  0.955324  0.323551 -0.436853 -1.889736
2020-02-29 -0.320544 -1.736806  1.244405 -2.053839
2020-03-01  0.719522 -1.927665  0.787947  0.422121
2020-03-02 -0.245060  0.407952  0.224241 -1.974252
'''
df = pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('abcd')) # np随机生成7行4列的集合 索引是日期 列名为abcd

'''
     A         B    C  D      E    F
0  1.0  20130102  1.0  3   test  foo
1  1.0  20130102  1.0  3  train  foo
2  1.0  20130102  1.0  3   test  foo
3  1.0  20130102  1.0  3  train  foo
'''
df2 = pd.DataFrame({'A': 1., 'B': '20130102','C': pd.Series(1, index=list(range(4)), dtype='float32'),'D': np.array([3] * 4, dtype='int32'),'E': ["test", "train", "test", "train"],'F': 'foo'})

#获取/查看数据
df['a']
df2.A
df[0:3] # 切片

df.head()
df2.tail(3)

# 标签选择
df.loc[dates[0]]
df.loc[:,['a']]
df.loc['20200225':'20200227',['a','b']] #切片
df.loc['20200225','a'] #获取具体值

#合并、分组、重塑
df3 = pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3], df[3:7], df[7:]]
#连接
'''
   key  a  b
0  foo  1  3
1  foo  1  4
2  foo  2  3
3  foo  2  4
'''
df4 = pd.merge(pd.DataFrame({'key':['foo','foo'],'a':[1,2]}),pd.DataFrame({'key':['foo','foo'],'b':[3,4]}),on = 'key')

#追加
df3.append(pd.DataFrame(np.random.randn(2,4)))

#分组
df.groupby('a').sum()

#可视化
pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000)).cumsum().plot()

# 数据输入输出
df4.to_csv('test_in.csv') # 写入csv
print(pd.read_csv('test_in.csv')) # 读取csv