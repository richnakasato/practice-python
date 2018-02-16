class DynamicArray(object):

    def __init__(self, start_capacity=1):
        self._size = 0
        self._capacity = start_capacity
        self._array = [None] * start_capacity

    def __len__(self):
        return self._size

    def __str__(self):
        return ', '.join(str(x) for x in self._array if x)

    def __getitem__(self, idx):
        if not 0 <= idx < self._size:
            raise IndexError('invalid index')
        return self._array[idx]

    def capacity(self):
        return self._capacity

    def size(self):
        return len(self)

    def get(self, idx):
        pass

    def append(self, val):
        self.add(self, self._size, val)

    def add(self, idx, val):
        if not 0 <= idx <= self._size:
            raise IndexError('invalid index')
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        if not idx == self._size:
            for i in range(self._size-1, idx, -1):
                self._array[i] = self._array[i-1]
        self._array[idx] = val
        self._size += 1

    def pop(self):
        return remove(self, self._size-1)

    def remove(self, idx):
        if not 0 <= idx < self._size:
            raise IndexError('invalid index')
        temp = self._array[idx]
        for i in range(idx, self._size-1):
            self._array[i] = self._array[i+1]
        self._array[self._size-1] = None
        self._size -= 1
        return temp

    def set(self, idx, val):
        pass

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        size = min(self._size, new_capacity)
        for i in range(size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
        self._size = size
