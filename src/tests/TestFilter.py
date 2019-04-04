
import unittest
from GamePhysics.SubLogic import Filter

class TestFilter(unittest.TestCase):
    def test1(self):
        self.assertEqual(Filter({"Gutsin": [4,3], "Adarsh": [1,2]}, 2), ["Gutsin", "Adarsh"])

    def test2(self):
        self.assertEqual(Filter({"Gutsin": [4,3], "Adarsh": [1,2]}, 1), ["Gutsin"])

    def test3(self):
        self.assertEqual(Filter({1: [4,3], "Adarsh": [1,2]}, 1), ["Adarsh"])

    def test4(self):
        self.assertEqual(Filter({},1), [])

    def test5(self):
        self.assertEqual(Filter({"Alpha": [0,1]},2), ["Alpha"])

if __name__ == '__main__':
    unittest.main()
