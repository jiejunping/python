"""
在Python中，这种一边循环一边计算的机制，称为生成器（Generator）

生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。
它不需要再写 __iter__()和 __next__()方法了，
只需要一个 yiled关键字。 生成器一定是迭代器（反之不成立）

特殊的地方是没用return 关键字,调用函数的返回值是生成器对象,
函数体中的代码并不会执行,只有显示或隐示地调用next的时候才会
真正执行里面的代码(可迭代对象:实现了 __iter__方法，
迭代器:实现了 __next__方法）)

函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

生成器在Python中是一个非常强大的编程结构，
可以用更少地中间变量写流式代码，此外，
相比其它容器对象它更能节省内存和CPU
但凡如下代码结构可以重构
def something():
    result = []
    for ... in ...:
        result.append(x)
    return result

def something():
    for ... in ...:
        yield x

generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
并在适当的条件结束for循环。对于函数改成的generator来说，
遇到return语句或者执行到函数体最后一行语句，
就是结束generator的指令，for循环随之结束

"""
import itertools


# 实现斐波那契数列
def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, cur+prev


f = fib()
print(list(itertools.islice(f, 0, 10)))


