import unittest
from your_script import process_data

class TestYourScript(unittest.TestCase):
    def test_example(self):
        # Example test case with the correct file path
        file_path = "sample_data.csv"
        result = process_data(file_path)  # Call your function with the file_path
        # Add a meaningful assertion for the test
        self.assertIsNotNone(result)  # Example assertion

if __name__ == "__main__":
    unittest.main()
