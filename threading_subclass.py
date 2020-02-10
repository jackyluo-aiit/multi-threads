import threading
from datetime import datetime
from time import sleep


def date_time_str(date_time):
    date_time_format = '%y-%M-%d %H:%M:%S'
    return datetime.strftime(date_time, date_time_format)


def loop(index, st):
    print(f'+++thread {index} start from:{date_time_str(datetime.now())}')
    sleep_time = st
    print(f'+++thread {index} sleep {sleep_time} seconds')
    sleep(sleep_time)
    print(f'+++thread {index} end sleeping at:{date_time_str(datetime.now())}')


class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.index = args[0]

    def run(self):
        print(f"Start to run:{self.index} at {date_time_str(datetime.now())}")
        self.func(*self.args)
        print(f"finished at {date_time_str(datetime.now())}")


def main():
    start = datetime.now()
    date_time_str(start)
    t1 = MyThread(loop, (1, 4))
    t2 = MyThread(loop, (2, 2))
    print(f'--------all threads start to run from:{date_time_str(start)}')
    t1.start()
    t2.start()
    print('+++main thread is waiting')
    t1.join()
    t2.join()
    end = datetime.now()
    date_time_str(end)
    print(f'--------all threads end at:{date_time_str(end)}, \n+++main thread run {end - start}')


if __name__ == '__main__':
    main()
