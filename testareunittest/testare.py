import unittest
import cal_average
class TestCase(unittest.TestCase):
    def test_average(self):
        result = cal_average.averager([20, 20])
        self.assertEqual(result , 20)
   


if __name__ == '__main__':
    unittest.main()
