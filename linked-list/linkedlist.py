class Node(object):

    """Docstring for Node. """

    def __init__(self, val=None, next=None):
        """TODO: to be defined1. """
        self._val = val
        self._next = next


class LinkedList(object):

    """Docstring for LinkedList. """

    def __init__(self, val=None, next=None):
        """TODO: to be defined1. """
        self._head = Node(val, next)

