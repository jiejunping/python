"""
列表(list)推导式
原理:
​   [表达式 for 变量 in 列表]
    L = [x ** 2 for x in L]
    1 循环变量表达式（ x ** 2）
    2 for 循环头部（ for x in L ）
工作原理
    Python在执行列表推导式时，会对可迭代对象 L 进行迭代，
    将每一次迭代的值赋给循环变量 x ，
    然后收集变量表达式 x ** 2 的计算结果，
    最终由这些结果构成了新的列表，也就是列表推导式所返回的值。
    要支持 for 循环进行迭代的对象，都可以对它使用列表推导式。
高级的扩展
　　１．在 for 语句后面跟上一个 if 判断语句，用于过滤掉那些不满足条件的结果项
　　２．以嵌套有多个 for 语句。按照从左至右的顺序，分别是外层循环到内层循环。
　　３．列表推导式可以带任意数量的嵌套 for 循环，并且每一个 for 循环后面都有可选的 if 语句　
字典(dict)推导式
    { key_expr: value_expr for value in collection if condition }
    字典推导式的外面也是使用花括号，不过花括号的内部需要包含键值两部分
集合(set)推导式
    集合推导式的语法与列表推导式相同，只需要把外面的方括号改成花括号即可
"""
L = [1, 2, 3, 4, 5]
L = [x**2 for x in L]
print(L)

L = [x**2 for x in L if x%2 != 0]
print(L)

L = [x+y for x in "ab" for y in "cd"]
print(L)

L = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(L)

dic = {'a': 10, 'b': 34}
dic = {v: k for k, v in dic.items()}
print(dic)



