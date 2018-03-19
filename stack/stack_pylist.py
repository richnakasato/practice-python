class StackPyList(object):

    """Stack implementation using Python lists."""

    def __init__(self):
        self._data = list()

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def top(self):
        if is_empty(self):
            raise IndexError('instance is empty')
        return self._data[len(self)-1]

    def is_empty(self):
        return (len(self) == 0)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError('instance is empty')
        self._data.pop(len(self)-1)
