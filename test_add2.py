import unittest
from math1 import add3

class TestAdd2(unittest.TestCase):
    def test_sum(self):  
        self.assertEqual(add2(1,1), 2)
        self.assertEqual(add2(0,0), 0)
        self.assertEqual(add2(2.34,2.34).__round__(2,2), 4)
        self.assertEqual(add2((1,2,3),(1,2,3)), (12))

    def test_negativeRadius(self):
        self.assertRaises(ValueError, add2, -2)

    def test_invalidType(self):
        self.assertRaises(TypeError, add2, 3+5j)        
        self.assertRaises(TypeError, add2, 'hello')
        self.assertRaises(TypeError, add2, None)        
        self.assertRaises(TypeError, add2, True)        
        self.assertRaises(TypeError, add2, False)
        self.assertRaises(TypeError, add2, [1,2,3])
        self.assertRaises(TypeError, add2, {"key": 1})

        print("Done.")
