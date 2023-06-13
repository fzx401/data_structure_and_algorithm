import queue
from collections import deque
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = deque()
    def push_back(self, value: int):
        """
        保证deque单调递减
        :param value:
        :return:
        """
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.queue.put(value)
        self.deque.append(value)
    def pop_front(self):
        if self.queue.empty():
            return -1
        res = self.queue.get()  # 注意不要轻易执行get方法
        if res == self.deque[0]:
            self.deque.popleft()
        return res
    def max_value(self):
        if not self.deque:
            return -1
        return self.deque[0]

q = MaxQueue()
q.push_back(1)
q.push_back(2)
q.max_value()
q.pop_front()