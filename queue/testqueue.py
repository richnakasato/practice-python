import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    """Docstring for TestQueue. """

    def project_should_do_something(self):
        """TODO: A test for project to do something. """
        x = Queue()
        self.assertNotEqual(x, None)


if __name__ == "__main__":
    unittest.main()
