import threading
import queue_demo
from time import sleep
from datetime import datetime


def date_time_str(date_time):
    date_time_format = '%y-%M-%d %H:%M:%S'
    return datetime.strftime(date_time, date_time_format)


class MyThread(threading.Thread):
    def __init__(self, index, q):
        super(MyThread, self).__init__()
        self.index = index
        self.q = q

    def run(self):
        while not self.q.empty():
            qlock.acquire()
            try:
                data = self.q.get(block=False)  # 当队列空的时候不再阻塞等待，而是报错: _queue.Empty
                print(f"thread {self.index} is processing on {data}, "
                      f"at {date_time_str(datetime.now())}")
                sleep(2)
                qlock.release()
            except Exception:
                print(f"thread {self.index} notices the queue is empty")
                qlock.release()


def main():
    workqueue = queue_demo.Queue()
    data = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
    qlock.acquire()
    print(f"+++main thread is assigning data into queue, "
          f"time: {date_time_str(datetime.now())}")
    for each in data:
        workqueue.put(each)
    qlock.release()
    print(f"+++main thread finished putting data into queue, t"
          f"ime: {date_time_str(datetime.now())}")
    t1 = MyThread(1, workqueue)
    t2 = MyThread(2, workqueue)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"main thread exit at {date_time_str(datetime.now())}")


if __name__ == '__main__':
    qlock = threading.Lock()
    main()
