import threading
from time import sleep

from datetime import datetime


def date_time_str(date_time):
    date_time_format = '%y-%m-%d %H:%M:%S'
    return datetime.strftime(date_time, date_time_format)


def work(index):
    signal.acquire()
    while True:
        print(f"thread {index} is working: {date_time_str(datetime.now())}")
        sleep(2)
        signal.notify()
        print(f"thread {index} is waiting: {date_time_str(datetime.now())}")
        signal.wait()
    signal.release()


if __name__ == '__main__':
    lock = threading.Lock()
    signal = con = threading.Condition()
    t1 = threading.Thread(target=work, args=(1,))
    t2 = threading.Thread(target=work, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
