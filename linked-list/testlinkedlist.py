import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    """Docstring for TestLinkedList. """

    def test_init(self):
        x = LinkedList(1)
        self.assertNotEqual(x, None)
        print(x._head._val)


if __name__ == "__main__":
    unittest.main()
