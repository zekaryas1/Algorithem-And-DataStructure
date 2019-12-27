from collections import deque

d = deque()  # or possible also to do deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
