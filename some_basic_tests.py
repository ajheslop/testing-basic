# Import unittest to write or tests
import unittest
# Import or basic function
from some_basic_code import my_basic_function 

# Unittest boilerplate
class TestStringMethods(unittest.TestCase):



    # And one test to pass
    def test_my_basic_function_passes(self):
        self.assertEqual(my_basic_function(), "Hi from my basic function!") # Pass!

if __name__ == '__main__':
    unittest.main()
