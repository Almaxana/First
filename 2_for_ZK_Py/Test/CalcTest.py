from unittest import TestCase, main
from lesson1.calculator import calculator


class CalcTest(TestCase):
    def test_plus (self):
        self.assertEqual(calculator(2, 3, '+'), 5)

    def test_minus (self):
        self.assertEqual(calculator(1, 7, '-'), -6)

    def test_multiply (self):
        self.assertEqual(calculator(2, 5, '*'), -10)


if __name__ == '__main__':
    main()
