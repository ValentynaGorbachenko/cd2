
def convertNumber(N):
    #checks type
    # print(N)
    # print (type(N) == int)
    if type(N) != int:
        return -1
    # checks if number can be returned
    if N<10 and N>=0:
        return N
    
    temp = str(N)
    str_res=""
    # print(type(temp))
    # updete temperary stirng
    for i in range(len(temp)-1, -1, -1):
        # print(temp[i])
        str_res = str_res + temp[i]
    # print(str_res)
    #return converted result
    return int(str_res)
    
    
# print(type(convertNumber(12345)))

# from path_to_the_file_name import covertNumber
import unittest

class ConvertNumberTest(unittest.TestCase):
    
    # @unittest.skip("demonstrating skipping")
    def test_check_type_of_input_string(self):
        # print(self.assertLogs())
        self.assertTrue(convertNumber("string") == -1, msg = 'trying to print message')
    
    # @unittest.skip("demonstrating skipping")   
    def test_check_type_of_input_number(self):
        self.assertEqual(type(convertNumber(123)), int)

    def test_check_type_of_input_number2(self):
        self.assertIsInstance(convertNumber(123), int)
        
    def test_convertion_of_number(self):
        self.assertEqual(convertNumber(12345), 54321)
        
    def test_converNumber_under_10(self):
        self.assertEqual(convertNumber(4), 4)
    
    # @unittest.skip
    def test_no_arguments_given(self):
        # self.assertEqual(convertNumber(21), 12)
        with self.assertRaises(TypeError, msg="TypeError is not here!"):
            convertNumber()
    
    @unittest.expectedFailure
    def test_no_argument(self):
        self.assertEqual(covertNumber(),2)

    @unittest.skip('example')
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """

        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)