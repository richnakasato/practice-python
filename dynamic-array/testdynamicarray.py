import unittest
from dynamicarray import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_init_should_create(self):
        x = DynamicArray()
        self.assertNotEqual(x, None)

    def test_init_size_should_be_zero(self):
        x = DynamicArray()
        self.assertEqual(x._size, 0)
        self.assertEqual(len(x), 0)

    def test_init_capacity_should_be_sixteen(self):
        x = DynamicArray()
        self.assertEqual(x._capacity, 16)

    def test_get_idx_checks_bounds(self):
        x = DynamicArray()
        with self.assertRaises(IndexError) as context:
            x.get(0)
        self.assertRaises(context.exception)

    def test_append_single_element(self):
        x = DynamicArray()
        x.append(99)
        self.assertEqual(x.get(0), 99)

    def test_add_single_element(self):
        x = DynamicArray()
        x.append(99)
        x.add(0, 100)
        x.add(1, 101)
        self.assertEqual(x.get(0), 100)
        self.assertNotEqual(x.get(1), 99)
        self.assertEqual(x.get(2), 99)
        self.assertEqual(x.size(), 3)
        x.print_self()

if __name__ == "__main__":
    unittest.main()
