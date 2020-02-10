from queue import Queue

q = Queue(3)  # 创建一个容量为3的队列
q.put(13, block=True, timeout=5)
q.put_nowait(23)
q.task_done()
print(q.get())
q.task_done()  # 如果没有对应put()的task_done()会join会一直阻塞
q.join()