import unittest
from unittest.mock import patch
import pandas as pd
from your_script import process_data  # Ensure your_script.py is in the same directory

class TestYourScript(unittest.TestCase):

    @patch('your_script.pd.read_csv')
    def test_example(self, mock_read_csv):
        # Mock the DataFrame that would be returned by pd.read_csv
        mock_data = pd.DataFrame({
            'Column1': [1, 2, 3],
            'Column2': [4, 5, 6],
        })
        mock_read_csv.return_value = mock_data

        # Define the file_path
        file_path = "sample_data.csv"
        result = process_data(file_path)  # Call your function with the file_path

        # Create expected Series with the correct name
        expected_mean_values = pd.Series([(1 + 4) / 2, (2 + 5) / 2, (3 + 6) / 2], name='Mean_Value')

        # Check if the new column exists
        self.assertTrue('Mean_Value' in result.columns)

        # Check values with the correct name
        pd.testing.assert_series_equal(result['Mean_Value'], expected_mean_values, check_names=True)

if __name__ == "__main__":
    unittest.main()
