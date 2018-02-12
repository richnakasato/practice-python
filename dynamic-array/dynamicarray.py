class DynamicArray(object):

    def __init__(self):
        self._size = 0
        self._capacity = 16
        self._array = [None]*16

    def __len__(self):
        return self._size

    def size(self):
        return self._size

    def get(self, idx):
        self._check_bounds(idx)
        return self._array[idx]

    def append(self, val):
        self.add(self._size, val)

    def add(self, idx, val):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        if idx == self._size: # append
            self._array[self._size] = val
            self._size += 1
        else: # normal add
            self._check_bounds(idx)
            for i in range(self._size, idx, -1):
                self._array[i] = self._array[i-1]
            self._array[idx] = val
            self._size += 1

    def pop(self):
        return self.remove(self._size-1)

    def remove(self, idx):
        ret_val = None
        last_added = self._size - 1
        self._check_bounds(idx)
        ret_val = self._array[idx]
        for i in range(idx, last_added):
            self._array[i] = self._array[i+1]
        self._array[last_added] = None
        self._size -= 1
        return ret_val

    def set(self, idx, val):
        self._check_bounds(idx)
        self._array[idx] = val

    def print_self(self):
        for i in range(self._size):
            print self._array[i]

    def _check_bounds(self, idx):
        if not (0 <= idx < self._size):
            raise IndexError('invalid index')

    def _resize(self, new_capacity):
        new_array = [None]*new_capacity
        size = min(self._size, new_capacity)
        for idx in range(size):
            new_array[idx] = self._array[idx]
        self._array = new_array
        self._capacity = new_capacity
