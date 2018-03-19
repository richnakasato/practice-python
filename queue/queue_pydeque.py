from collections import deque

class QueuePyDeque(object):

    """Queue implementation using Python deque."""

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def front(self):
        if is_empty(self):
            raise IndexError('instance is empty')
        return self._data[0]

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if is_empty(self):
            raise IndexError('instance is empty')
        self._data.popleft()
