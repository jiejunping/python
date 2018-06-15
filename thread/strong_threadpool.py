import threading, queue, contextlib, time

stopFlag = object();


class ThreadPool(object):

    def __init__(self, max_num):
        self.queue = queue.Queue()
        self.max_num = max_num

        # 是否立即终止标志
        self.terminal = False
        # 当前已经创建的线程对象列表
        self.queue_real_list_list = []
        # 空闲的线程对象列表
        self.queue_free_list = []

    def run(self, target, args, callback):
        # 将线程要执行的功能函数和回调函数打包成任务元组
        task_tuple = (target, args, callback)
        self.queue.put(task_tuple)
        # 判断空闲列表是否为空且真实的线程列表数目是否小于最大线程数目, 若是则执行add_thread()函数添加线程
        if len(self.queue_free_list) == 0 and len(self.queue_real_list_list) < self.max_num:
            self.add_thread()

    def add_thread(self):
        thread = threading.Thread(target=self.fetch)
        thread.start()

    def fetch(self):
        current_thread = threading.currentThread()
        self.queue_real_list_list.append(current_thread)
        task_tuple = self.queue.get()
        func, args, callback = task_tuple
        while task_tuple != stopFlag:
            result_status = True
            try:
                result = func(args)
            except Exception as e:
                result_status = False
                result = e
            if callback is not None:
                try:
                    callback(result_status, result)
                except Exception as  e:
                    pass
            # 是否立即终止当前线程
            if not self.terminal:
                # 1加入空闲的线程对象列表
                # 2从任务队列中取出任务元组
                # 3等待当前线程执行完任何立即结束
                with ThreadPool.queue_operate(self.queue_free_list, current_thread):
                    task_tuple = self.queue.get()
            else:
                task_tuple = stopFlag
        else:
            self.queue_real_list_list.remove(current_thread)

    def close(self):
        num = len(self.queue_real_list_list)
        while num:
            self.queue.put(stopFlag)
            num -= 1

    def terminate(self):
        self.terminal = True
        self.close()

    def terminate_clean_queue(self):
        self.terminal = True
        while self.queue_real_list_list:
            self.queue.put(stopFlag)
        self.queue.empty()

    """
    简化上下文管理
    
    @contextmanager这个decorator接受一个generator，
    用yield语句把with ... as var把变量输出出去，
    然后，with语句就可以正常地工作了
    
    代码执行顺序:
    1.with语句首先执行yield之前的语句
    2.yield调用会执行with语句内部的所有语句
    3.最后执行yield之后的语句
    
    """

    @staticmethod
    @contextlib.contextmanager
    def queue_operate(ls, ct):
        ls.append(ct)
        try:
            yield
        finally:
            ls.remove(ct)


def callback_func(result_status, result):
        print("callback_func")
        print(result)
        print(result_status, result)


def test(i):
    time.sleep(1)
    return "current thread is: {}".format(i)


if __name__ == "__main__":
    pool = ThreadPool(5)
    for tmp in range(20):
        pool.run(target=test, args=(tmp,), callback=callback_func)
    # pool.terminate()
