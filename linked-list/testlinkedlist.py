import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    """Docstring for TestLinkedList. """

    def test_init(self):
        x = LinkedList(1)
        self.assertNotEqual(x, None)
        self.assertEqual(len(x), 1)

    def test_insert(self):
        x = LinkedList(0)
        print(str(x))
        x.insert(0, 10)
        x.insert(0, 20)
        x.insert(0, 30)
        x.insert(0, 40)
        self.assertEqual(len(x), 5)
        x.insert(1, 50)
        print(str(x))
        x.insert(6, 50)
        print(str(x))

    def test_remove(self):
        x = LinkedList(0)
        print(str(x))
        x.remove(0)
        with self.assertRaises(IndexError):
            x.remove(0)
        x.insert(0, 10)
        x.insert(0, 20)
        x.remove(0)
        self.assertEqual(x.get(0), 10)
        print(str(x))
        x.insert(0, 30)
        x.insert(0, 40)
        x.remove(0)
        print(str(x))
        self.assertEqual(x.get(0), 30)
        x.remove(1)
        print(str(x))
        self.assertEqual(x.get(0), 30)

if __name__ == "__main__":
    unittest.main()
