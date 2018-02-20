class Node(object):

    """Docstring for Node. """

    def __init__(self, element=None, next=None):
        """TODO: to be defined1. """
        self._element = element
        self._next = next


class LinkedList(object):

    """Docstring for LinkedList. """

    def __init__(self, element=None, next=None):
        """TODO: to be defined1. """
        self._head = Node(element, next)

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

    def size(self):
        return len(self)

    def insert(self, idx=0, element=None):
        if idx == 0:
            new_head = Node(element, self._head)
            self._head = new_head
            return
        count = 1
        prev = self._head
        while prev:
            if count == idx:
                to_insert = Node(element, prev._next)
                prev._next = to_insert
                return
            prev = prev._next
            count += 1
        raise IndexError('invalid index')


