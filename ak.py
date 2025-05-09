from collections import deque
list = [1,2,3,4,5]
d = deque(list)
print(d)
d.popleft()
print(d)