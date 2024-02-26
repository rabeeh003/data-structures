# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.pop()
# print(stack)


# # using deque from collection
# from collections import deque

# stack = deque()
# stack.append(12)
# stack.append(13)
# stack.append(14)
# stack.pop()
# print(stack)


# using LifoQueue
# from queue import LifoQueue

# stack = LifoQueue()
# stack.put(10)
# stack.put(100)
# stack.put(1000)
# print(stack.get())
# print(stack.get())


# re...

# stack = ["a", "b", "c", "d"]
# r = len(stack)-1 
# l = 0
# while l < r:
#     stack[l], stack[r] = stack[r], stack[l]
#     l += 1
#     r -= 1
# print(stack)


st = "hello"
kk = []
rev = '' 
for i in st:
    kk.append(i)
while kk:
    rev += kk.pop()
print(st)
print(rev)


stack = []
stack.append(12)
stack.append(22)
stack.append(32)
stack.pop()
print(stack)

string = 'hello world'
temp = []
cs = ''
for i in string:
    temp.append(i)
while temp:
    cs += temp.pop()
print(cs)