
import unittest
from GamePhysics.SubLogic import Elimination

class TestElimination(unittest.TestCase):
    def test1(self):
        self.assertEqual(Elimination({"Adarsh": [4,3], "Gutsin": [4,3], "SirHype": ["A"]}, "Adarsh"),
                         {"Gutsin": [4,3], "SirHype": ["A"]})

    def test2(self):
        self.assertEqual(Elimination({"Gutsin": [4,3], "lol": ["A"]}, "lol"),
                         {"Gutsin": [4,3]})

    def test3(self):
        self.assertEqual(Elimination({"Gutsin": [4,3], 1: ["A"]}, 1),
                         {"Gutsin": [4,3]})
    def test4(self):
        self.assertEqual(Elimination({}, "Alpha"),
                         {})

    def test5(self):
        self.assertEqual(Elimination({1:2, 3:4}, 1),
                         {})

if __name__ == '__main__':
    unittest.main()
