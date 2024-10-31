import unittest from your_script import 
your_function_name class 
TestYourScript(unittest.TestCase):
    def test_example(self):
        # مثال از تست یک تابع
        result = your_function_name() 
        self.assertEqual(result, 'انتظار 
        خروجی')
if __name__ == '__main__':
    unittest.main()
