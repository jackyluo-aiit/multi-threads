import _thread
from time import sleep
from datetime import datetime

date_time_format = '%y-%M-%d %H:%M:%S'


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


# print(date_time_str(datetime.now()))  # test date time


def loop_one():
    print(f'+++thread 1 start from:{date_time_str(datetime.now())}')
    sleep_time = 3
    print(f'+++thread 1 sleep {sleep_time} seconds')
    sleep(sleep_time)
    print(f'+++thread 1 end sleeping at:{date_time_str(datetime.now())}')


def loop_two():
    print(f'+++thread 2 start from:{date_time_str(datetime.now())}')
    sleep_time = 2
    print(f'+++thread 2 sleep {sleep_time} seconds')
    sleep(sleep_time)
    print(f'+++thread 2 end sleeping at:{date_time_str(datetime.now())}')


def main():
    start = datetime.now()
    date_time_str(start)
    print(f'--------all threads start to run from:{date_time_str(start)}')
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    end = datetime.now()
    date_time_str(end)
    print(f'--------all threads end at:{date_time_str(end)}, \n+++main thread run {end-start}')


if __name__ == '__main__':
    main()
