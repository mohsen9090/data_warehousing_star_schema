import unittest
from your_script import process_data  # Import the function from your_script.py

class TestYourScript(unittest.TestCase):
    def test_example(self):
        # Provide the path to your sample CSV file
        file_path = "sample_data.csv"  # Make sure this file exists
        result = process_data(file_path)  # Call the function with the file path
        
        # Example assertion to ensure the function runs correctly
        self.assertIsNotNone(result)  # Check if the result is not None

if __name__ == "__main__":
    unittest.main()
