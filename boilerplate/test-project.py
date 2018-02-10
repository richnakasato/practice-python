import unittest
from project import Project


class TestProject(unittest.TestCase):

    """Docstring for TestProject. """

    def project_should_do_something(self):
        """TODO: A test for project to do something. """
        x = Project()
        self.assertNotEqual(x, None)


if __name__ == "__main__":
    unittest.main()
