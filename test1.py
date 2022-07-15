from string import whitespace
from unittest import TestCase, main
from hw_unit_test import remove_zeros

# Acceptance Criteria
    # The 'remove_zeros' function only accepts a list of integers.
    # It should reject anything that isn't a list, or a list that contains more than just integers (float, string, etc.).
    # The function should also reject an empty list.

class ZerosRemovedTest(TestCase):
    def test_1_base(self):
        self.assertEqual(remove_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_2_base(self):
        self.assertEqual(remove_zeros([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]), [1, 7, 8, 10, 12, 4, 0, 0, 0, 0])

    def test_3_base(self):
        # no zeroes in list
        self.assertEqual(remove_zeros([1,2,8,4,5,6,1]), [1,2,8,4,5,6,1])

    def test_4_base(self):
        # all zeros in list
        self.assertEqual(remove_zeros([0,0,0,]), [0,0,0,])

    def test_5_not_a_list(self):
        #testing string
        self.assertEqual(remove_zeros("I'm gonna make him an offer he can't refuse."), 'Not a list, try again.')

        #testing tuple
        self.assertEqual(remove_zeros((1,5,6,8,14,0,0,0,)), 'Not a list, try again.')

        #testing (negative) integer
        self.assertEqual(remove_zeros(-651698), 'Not a list, try again.')

        #testing float
        self.assertEqual(remove_zeros(3.14159265359), 'Not a list, try again.')

    def test_6_list_contains_non_int(self):
        # list contains mix of integers, float, and string
        self.assertEqual(remove_zeros([1,0, False, 2,3,-5, 8.2, 'death', 'before', 'decaf']), 'This list contains non-integers. Please provide a list that only contains integers.')

        # empty list 
        self.assertEqual(remove_zeros([]), 'List is empty, try again.')

    def test_7_contains_whitespace(self):
        # Integers unaffected by whitespace
        self.assertEqual(remove_zeros([0,1    , 5  , 6,    5  ,]), [1,5,6,5,0])
        

    