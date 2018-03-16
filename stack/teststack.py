import unittest
from stack import Stack
from stack_pylist import StackPyList


class TestStack(unittest.TestCase):

    def test_pylist_init(self):
        x = StackPyList()
        self.assertNotEqual(x, None)

    def test_pylist_add(self):
        x = StackPyList()
        x.push(1)
        x.push(2)
        x.push(3)
        x.push(4)
        x.push(5)
        self.assertEqual(x.top(), 5)
        x.pop()
        self.assertEqual(x.top(), 4)
        x.pop()
        self.assertEqual(x.top(), 3)
        x.pop()
        self.assertEqual(x.top(), 2)
        x.pop()
        self.assertEqual(x.top(), 1)


if __name__ == "__main__":
    unittest.main()
