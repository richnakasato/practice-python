import unittest
from dynamicarray import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_init(self):
        x = DynamicArray(16)
        self.assertNotEqual(x, None)
        self.assertEqual(len(x), 0)
        self.assertEqual(x.capacity(), 16)

    def test_add(self):
        x = DynamicArray()
        with self.assertRaises(IndexError):
            x.add(len(x)+1, 1)
        x.add(len(x), 1)
        x.add(len(x), 2)
        self.assertEqual(x[1], 2)
        self.assertEqual(x[0], 1)
        self.assertEqual(x.capacity(), 2)
        self.assertEqual(len(x), 2)

    def test_resize(self):
        x = DynamicArray()
        x.add(len(x), 1)
        x.add(len(x), 2)
        x.resize(1)
        with self.assertRaises(IndexError):
            x.add(x[1], 2)
        self.assertEqual(x[0], 1)
        self.assertEqual(x.capacity(), 1)
        self.assertEqual(len(x), 1)

    def test_remove(self):
        x = DynamicArray()
        x.add(len(x), 1)
        x.add(len(x), 2)
        x.remove(1)
        with self.assertRaises(IndexError):
            x.remove(1)
        self.assertEqual(x[0], 1)
        self.assertEqual(x.capacity(), 2)
        self.assertEqual(len(x), 1)

    def test_init_size_should_be_zero(self):
        pass

    def test_init_capacity_should_be_sixteen(self):
        pass

    def test_get_idx_checks_bounds(self):
        pass

    def test_append_single_element(self):
        pass

    def test_add_single_element(self):
        pass

if __name__ == "__main__":
    unittest.main()
