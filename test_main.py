import unittest
from unittest import mock
from main import h_feet_input, h_inches_input, p_weight_input, bmi_calc

class TestBMI(unittest.TestCase):
    
    #testing if feet input works
    def test_h_feet_input(self):

        #testing min number
        with unittest.mock.patch('builtins.input', return_value = '0'):
            self.assertEqual(h_feet_input(), 0.0)

        #testing average number
        with unittest.mock.patch('builtins.input', return_value='5'):
            self.assertEqual(h_feet_input(), 5.0)
        
        #testing non numerical input
        with unittest.mock.patch('builtins.input', return_value='hello'):
            with self.assertRaises(ValueError):
                h_feet_input()
    
    #testing if inches input works
    def test_h_inches_input(self):

        #testing min number
        with unittest.mock.patch('builtins.input', return_value = '0'):
            self.assertEqual(h_inches_input(), 0.0)


        #testing normal number
        with unittest.mock.patch('builtins.input', return_value='8'):
            self.assertEqual(h_inches_input(), 8.0)

        #testing max number
        with unittest.mock.patch('builtins.input', return_value='12'):
            self.assertEqual(h_inches_input(), 12.0)
        
        #testing non numerical input
        with unittest.mock.patch('builtins.input', return_value='hello'):
            with self.assertRaises(ValueError):
                h_inches_input()
    
    #testing if weight input works
    def test_p_weight_input(self):

        #testing min number
        with unittest.mock.patch('builtins.input', return_value = '0'):
            self.assertEqual(p_weight_input(), 0.0)

        #testing a normal number
        with unittest.mock.patch('builtins.input', return_value='150'):
            self.assertEqual(p_weight_input(), 150.0)
        
        #testing non numerical input
        with unittest.mock.patch('builtins.input', return_value='hello'):
            with self.assertRaises(ValueError):
                p_weight_input()
    

    #testing if the calculator works in general, all should return TRUE
    def test_bmi_calc(self):

        # #testing underweight
        # self.assertEqual(round(bmi_calc(5, 0, 100),1), 20.0)
        
        # #testing normal weight
        # self.assertEqual(round(bmi_calc(5, 10, 150),1), 22.0)
        
        # #testing overweight
        # self.assertEqual(round(bmi_calc(6, 0, 200),1), 27.8)
        
        # #testing obese
        # self.assertEqual(round(bmi_calc(5, 8, 250),1), 38.9)

        #testing edge cases

        #lowest edge
        #Underweight is <18.5
        self.assertEqual(bmi_calc(5, 10, 125), "Underweight")
        self.assertEqual(bmi_calc(5, 9, 123), "Normal")

        #upper edge of normal/lower edge of overweight
        #Normal max is 24.9
        self.assertEqual(bmi_calc(5, 10, 169.5), "Normal")
        self.assertEqual(bmi_calc(5, 10, 170), "Overweight")

        #upper edge of overweight/lower edge of obese
        #Overweight max is 29.9
        self.assertEqual(bmi_calc(5, 10, 203.5), "Overweight")
        self.assertEqual(bmi_calc(5, 10, 204), "Obese")

if __name__ == '__main__':
    unittest.main()
