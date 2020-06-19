import unittest
from LatticePaths import lattice_paths, main as LP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("137846528820",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(lattice_paths(4,2),15)
        self.assertEqual(lattice_paths(3,3),20)

    def test_value_errors(self):
        self.assertRaises(ValueError, lattice_paths, -1,1)
        self.assertRaises(ValueError, lattice_paths, 100,1)
        self.assertRaises(ValueError, lattice_paths, 0,1)
        self.assertRaises(ValueError, lattice_paths, 1,-1)
        self.assertRaises(ValueError, lattice_paths, 1,100)
        self.assertRaises(ValueError, lattice_paths, 1,0)

    def test_type_errors(self):
        self.assertRaises(TypeError, lattice_paths, "Test",1)
        self.assertRaises(TypeError, lattice_paths, 3+5j,1)
        self.assertRaises(TypeError, lattice_paths, 1,0,1)

if __name__ == '__main__':
    unittest.main()