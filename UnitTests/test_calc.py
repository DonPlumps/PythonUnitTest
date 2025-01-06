import unittest
import src.calc as calc

class TestCalc(unittest.TestCase):

    def test_calc_bmi_functionality(self):
        self.assertEqual(calc.calc_bmi(70, 1.75),22.86)


    def test_calc_bmi_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calc.calc_bmi(70, 0)


    def test_calc_bmi_negative_numbers(self):
        with self.assertRaises(ValueError):
            calc.calc_bmi(70, -2)
        with self.assertRaises(ValueError):
            calc.calc_bmi(-70, 2)
        with self.assertRaises(ValueError):
            calc.calc_bmi(-70, -2)


    def test_calc_bmi_type(self):
        with self.assertRaises(TypeError):
            calc.calc_bmi("hamster", 2)
        with self.assertRaises(TypeError):
            calc.calc_bmi(70, "2")

if __name__ == "__main__":
    unittest.main()
