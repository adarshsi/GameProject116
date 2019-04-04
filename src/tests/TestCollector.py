
import unittest
from GamePhysics.SubLogic import SpermCollector

class TestCollector(unittest.TestCase):
    def test1(self):
        self.assertEqual(SpermCollector({"Adarsh": [4,3], "Gutsin": [4,3], "SirHype": ["A"]}), ["Adarsh", "Gutsin"])

    def test2(self):
        self.assertEqual(SpermCollector({}), [])

    def test3(self):
        self.assertEqual(SpermCollector({"Adarsh": [], "Gutsin": [], "SirHype": [3,4,3]}), [])

    def test4(self):
        self.assertEqual(SpermCollector({"Adarsh": [], "Gutsin": [], "SirHype": [4,3]}), ["SirHype"])

if __name__ == '__main__':
    unittest.main()