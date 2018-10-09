from functools import reduce
"""
lambda 开头,之后就是函数的参数列表,并以":"结尾,
紧接着就是表达式主体,整个只有一行语句

一般创建匿名函数时候使用lamdba表达式

"""
g = lambda x, y: x+y
print(g(1, 2))

"""
内置的map函数，两个参数，第一个是一个函数； 第二个是一个可遍历的对象
map函数将第二个参数里的每个元素依次传给作为第一个参数的函数，并将函数
的返回值依顺序组成一个列表

map(),filter()这些的返回值已经不再是list,而是iterators, 
所以想要使用，只用将iterator 转换成list 即可

filter 函数，用来做刷选的，会根据第一个参数的函数的返回值来剔出

reduce 是用来做聚合运算

"""

listData = range(5)
print(list(map(lambda x: x+1, listData)))

# print([i+1 for i in listData])

print(list(filter(lambda x: x%2 == 0, listData)))

print(list(listData))
print(reduce(lambda accumvalue, newvalue:accumvalue+newvalue,listData, 1))


