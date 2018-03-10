class Node(object):

    def __init__(self, new_element=None, new_next=None):
        self._element = new_element
        self._next = new_next


class LinkedList(object):

    def __init__(self):
        self._head = None

    def __len__(self):
        count = 0
        traverse = self._head
        while traverse:
            traverse = traverse._next
            count += 1
        return count

    def __str__(self):
        output = list()
        traverse = self._head
        while traverse:
            output.append(str(traverse._element))
            traverse = traverse._next
        return ' '.join(output)

    def __getitem__(self, idx):
        count = 0
        traverse = self._head
        while traverse:
            if count == idx:
                return traverse._element
            traverse = traverse._next
            count += 1
        raise IndexError('invalid index')

    def size(self):
        return len(self)

    def get(self, idx):
        return self[idx]

    def set(self, idx, new_element):
        count = 0
        traverse = self._head
        while traverse:
            if count == idx:
                traverse._element = new_element
                return
            traverse = traverse._next
            count += 1
        raise IndexError('invalid index')

    def add(self, idx=0, new_element):
        if idx == 0:
            new_head = Node(new_element, self._head)
            self._head = new_head
            return
        count = 1
        prev = self._head
        while prev:
            if count == idx:
                to_insert = Node(new_element, prev._next)
                prev._next = to_insert
                return
            prev = prev._next
            count += 1
        raise IndexError('invalid index')

    def remove(self, idx=0):
        if idx == 0:
            self._head = self._head._next
            return
        count = 1
        prev = self._head
        while prev._next:
            if count == idx:
                prev._next = prev._next._next
                return
            prev = prev._next
            count += 1
        raise IndexError('invalid index')

