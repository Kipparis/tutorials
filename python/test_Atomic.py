import unittest

class TestAtomic(unittest.TestCase):
    def setUp(self):
        self.original_list = list(range(10))
