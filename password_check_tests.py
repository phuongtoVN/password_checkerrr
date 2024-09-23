import unittest
from password_checker import check_password_strength, interpret_score, evaluate_password

class TestPasswordChecker(unittest.TestCase):

    def test_check_password_strength(self):
        self.assertEqual(check_password_strength("password"), 2)
        self.assertEqual(check_password_strength("Password1"), 4)
        self.assertEqual(check_password_strength("P@ssw0rd"), 5)
        self.assertEqual(check_password_strength("a"), 1)

    def test_interpret_score(self):
        self.assertEqual(interpret_score(1), "Weak")
        self.assertEqual(interpret_score(3), "Moderate")
        self.assertEqual(interpret_score(5), "Strong")

    def test_evaluate_password(self):
        self.assertEqual(evaluate_password("password"), (2, "Weak"))
        self.assertEqual(evaluate_password("Password1"), (4, "Moderate"))
        self.assertEqual(evaluate_password("P@ssw0rd"), (5, "Strong"))

if __name__ == '__main__':
    unittest.main()