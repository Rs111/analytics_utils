import unittest
from analytics_utils.date import validate


class TestValidate(unittest.TestCase):

    # should return true for a valid '%Y-%m-%d' format string
    def test_valid_standard_date(self):
        self.assertEqual(validate('2019-01-01', '%Y-%m-%d'), True)

    # should return false when day is greater than 31
    def test_day_gt_31(self):
        self.assertEqual(validate('2019-01-34', '%Y-%m-%d'), False)

    # should return false when day is one digit
    def test_day_eq_9(self):
        self.assertEqual(validate('2019-01-9', '%Y-%m-%d'), False)

    # should return false when day is 00
    def test_day_eq_00(self):
        self.assertEqual(validate('2019-01-00', '%Y-%m-%d'), False)

    # should return false when month is greater than 12
    def test_month_gt_12(self):
        self.assertEqual(validate('2019-13-34', '%Y-%m-%d'), False)

    # should return false when month is one digit
    def test_month_eq_5(self):
        self.assertEqual(validate('2019-5-09', '%Y-%m-%d'), False)

    # should return false when month is 00
    def test_month_eq_00(self):
        self.assertEqual(validate('2019-13-34', '%Y-%m-%d'), False)

    # should return false when year is not 4 digits
    def test_year_eq_200(self):
        self.assertEqual(validate('200-5-09', '%Y-%m-%d'), False)

    # should return false when string contains a special character format string
    def test_special_character(self):
        self.assertEqual(validate('2019-01-01#', '%Y-%m-%d'), False)

    # should return false when string contains a letter
    def test_letter_character(self):
        self.assertEqual(validate('2019-01a-01', '%Y-%m-%d'), False)


if __name__ == '__main__':
    unittest.main()
