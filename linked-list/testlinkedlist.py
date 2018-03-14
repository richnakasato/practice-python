import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_init(self):
        x = LinkedList()
        self.assertNotEqual(x, None)
        self.assertEqual(len(x), 0)

    def test_add(self):
        x = LinkedList()
        x.add(0, 0)
        x.add(0, 10)
        x.add(0, 20)
        x.add(0, 30)
        x.add(0, 40)
        print(str(x))
        self.assertEqual(len(x), 5)
        x.add(1, 50)
        print(str(x))
        x.add(6, 60) # appending
        print(str(x))
        with self.assertRaises(IndexError):
            x.add(100, 100)

    def test_remove(self):
        x = LinkedList()
        with self.assertRaises(IndexError):
            x.remove(0)
        x.add(0, 10)
        x.add(0, 20)
        x.remove(0)
        print(str(x))
        self.assertEqual(x.get(0), 10)
        x.add(0, 30)
        x.add(0, 40)
        x.remove(0)
        print(str(x))
        self.assertEqual(x.get(0), 30)
        x.remove(1)
        print(str(x))
        self.assertEqual(x.get(0), 30)

if __name__ == "__main__":
    unittest.main()
