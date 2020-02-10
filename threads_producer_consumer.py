import threading
from time import sleep

con = threading.Condition()
global meat
meat = 0


def consumer():
    global meat
    con.acquire()
    while True:
        meat -= 1
        print(f"------Eating, meat:{meat}")
        sleep(2)
        if meat == 0:
            print("------Please add more meat")
            con.notify()
            con.wait()
    con.release()


def producer():
    global meat
    con.acquire()
    while True:
        meat += 1
        if meat == 10:
            print("++++++Adding eat, please wait")
            sleep(2)
            print(f"++++++Please Eat meat, meat:{meat}")
            con.notify()
            con.wait()
    con.release()


if __name__ == '__main__':
    producer1 = threading.Thread(target=producer, args=())
    consumer1 = threading.Thread(target=consumer, args=())

    producer1.start()
    consumer1.start()

    producer1.join()
    consumer1.join()
