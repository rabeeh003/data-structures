que = []

que.append(1)
que.append(10)
que.append(100)
que.pop(0)
print(que)

# using collection.deque
from collections import deque

que = deque()
que.append(10)
que.append(20)
que.append(30)
que.popleft()
print(que)

# using queue.Queue
# from queue import LifoQueue

# pooda = LifoQueue()
# pooda.put(12)
# pooda.put(123)
# pooda.put(1234)
# print(pooda.get())
# print(pooda.get())


qu = []
qu.append(12)
qu.append(22)
qu.append(32)
qu.pop(0)
print(qu)
