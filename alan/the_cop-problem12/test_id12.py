import id12   # The code to test
import unittest   # The test framework

class Test_Problem12(unittest.TestCase):
    def test_calculate_1(self):
        testsum=500
        begin_triangle_number=8 
        output_data=76576500
        self.assertEqual(id12.calculate_divisors(testsum,begin_triangle_number), output_data)

    def test_calculate_2(self):
        testsum=0
        begin_triangle_number=8 
        output_data=36
        self.assertEqual(id12.calculate_divisors(testsum,begin_triangle_number), output_data)


if __name__ == '__main__':
    unittest.main()