import queue
import threading
from time import sleep

global workqueue
workqueue = queue.Queue(10)

con = threading.Condition()


def consumer():
    con.acquire()
    global workqueue
    while True:
        if not workqueue.empty():
            work = workqueue.get(block=False)
            print(f"---consumer is working {work}")
            sleep(2)
        else:
            print("---Finished work")
            con.notify()
            con.wait()


def producer():
    con.acquire()
    global workqueue
    count = 0
    while True:
        if count % 10 == 0:
            con.notify()
            con.wait()
        print(f"+++producer is adding work: {count}")
        sleep(2)
        workqueue.put_nowait(count)
        count += 1
    con.release()


if __name__ == '__main__':
    producer1 = threading.Thread(target=producer, args=())
    consumer1 = threading.Thread(target=consumer, args=())

    producer1.start()
    consumer1.start()

    producer1.join()
    consumer1.join()
