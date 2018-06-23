# 不带参数的
def outer1(func):
    print("outer 开始执行")

    def inner():
        print("认证成功")
        result = func()
        print("日志添加成功")
        return result
    return inner


# 带参数的
def outer2(func):
    print("outer 带参数的装饰器开始执行")

    # 参数arg、*args、 ** kwargs三个参数的位置必须是一定的。必须是(arg, *args, **kwargs) 这个顺序
    # *args 用来将参数打包成tuple给函数体调用，**kwargs 打包关键字参数成dict给函数体调用
    def inner(*args,**kwargs):
        print("带参数的认证成功")
        result = func(*args,**kwargs)
        print("带参数的日志添加成功")
        return result
    return inner


@outer1
@outer2
def f1():
    print("业务部门1数据接口......")


@outer2
def f2(name,age):
    print("%s 正在连接业务部门1数据接口......"%name)


f1()
f2("jack",20)

"""
执行结果
outer 带参数的装饰器开始执行
outer 带参数的装饰器开始执行
认证成功
业务部门1数据接口......
日志添加成功
认证成功
jack 正在连接业务部门1数据接口......
日志添加成功
"""

"""
装饰器执行顺序说明：

1.被装饰的函数的名字会被当作参数传递给装饰函数，装饰函数执行内部代码后，

2.将它的返回值赋值给被装饰的函数，f1指向的函数地址发生改变，f1 = inner
(函数内存地址：　当函数体被读进内存后的保存位置，它由标识符即函数名引用)

3.在往后调用f1的时候，执行inner函数内部代码；

4.在inner函数体中，func这个量保存了老的函数在内存中的地址，通过它就可以执行 老的函数体体

5. inner 函数返回的值是func函数执行的结果。供r = f1的方式接收

装饰函数体现的是一种设计模式，强调的是开放封闭原则，
更多的用于后期功能升级而不是编写新的代码。
装饰器不光能装饰函数，也能装饰其他的对象，比如类

"""