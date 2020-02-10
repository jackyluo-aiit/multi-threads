import threading
from time import sleep
from datetime import datetime


def date_time_str(date_time):
    date_time_format = '%y-%M-%d %H:%M:%S'
    return datetime.strftime(date_time, date_time_format)


class MyThread(threading.Thread):
    counter = 6

    def __init__(self, index):
        super(MyThread, self).__init__()
        self.index = index

    def run(self, count=3):
        lock.acquire()
        for i in range(count):
            sleep(1)
            print(f"thread {self.index} is working at {date_time_str(datetime.now())}"
                  f", counter: {MyThread.counter}")
            MyThread.counter -= 1
        lock.release()


def main():
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()


if __name__ == '__main__':
    lock = threading.Lock()
    main()
