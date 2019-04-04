
import unittest
from GamePhysics.SubLogic import checkHole

class TestHole(unittest.TestCase):
    def test1(self):
        self.assertEqual(checkHole({"Gutsin": [4,3], "Adarsh": [1,2]}, [1,2]),
                         {"Gutsin": [4,3]})

    def test2(self):
        self.assertEqual(checkHole({"Adarsh": [4,3], "Gutsin": [4,3], "SirHype": []}, [4,3]),
                         {})

    def test3(self):
        self.assertEqual(checkHole({"Gutsin": [4,3], 1: ["A"]}, 1),
                         {"Gutsin": [4,3]})

    def test4(self):
        self.assertEqual(checkHole({"Alpha": [], "Beta": []}, []),
                         {})

    def test5(self):
        self.assertEqual(checkHole({"Gutsin": [4,3], "Adarsh": [4,3]}, [4,3]),
                         {})

if __name__ == '__main__':
    unittest.main()
