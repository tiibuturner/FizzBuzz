import unittest
import FizzBuzzEngine

class MyFizzBuzTest(unittest.TestCase):
    def test_Send_1_To_FizzBuzzEngine_Result_1(self):
        value = int(1)
        expectedResult = int(1)

        result = FizzBuzzEngine.resultOutput(value)

        self.assertEqual(result, expectedResult)
    
    def test_Send_2_To_FizzBuzzEngine_Result_2(self):
        value = int(2)
        expectedResult = int(2)

        result = FizzBuzzEngine.resultOutput(value)
        
        self.assertEqual(result, expectedResult)

    def test_Send_3_To_FizzBuzzEngine_Result_3(self):
        value = int(3)
        expectedResult = 'Fizz'

        result = FizzBuzzEngine.resultOutput(value)
        
        self.assertEqual(result, expectedResult)

    def test_Send_4_To_FizzBuzzEngine_Result_4(self):
        value = int(4)
        expectedResult = int(4)

        result = FizzBuzzEngine.resultOutput(value)
        
        self.assertEqual(result, expectedResult)

    def test_Send_15_To_FizzBuzzEngine_Result_15(self):
        value = int(15)
        expectedResult = 'FizzBuzz'

        result = FizzBuzzEngine.resultOutput(value)
        
        self.assertEqual(result, expectedResult)

if (__name__ == "__main__"):
    unittest.main()