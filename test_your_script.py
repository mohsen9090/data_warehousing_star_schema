import unittest
from unittest.mock import patch
import pandas as pd
from your_script import process_data

class TestYourScript(unittest.TestCase):
    
    @patch('your_script.pd.read_csv')
    def test_example(self, mock_read_csv):
        # Mocking the DataFrame that would be returned by pd.read_csv
        mock_data = pd.DataFrame({
            'Column1': [1, 2, 3],
            'Column2': [4, 5, 6],
        })
        mock_read_csv.return_value = mock_data
        
        file_path = "sample_data.csv"  # Define the file_path
        result = process_data(file_path)  # Call your function with the file_path
        
        # Check if the 'Mean_Value' column is calculated correctly
        expected_mean_values = pd.Series([(1 + 4) / 2, (2 + 5) / 2, (3 + 6) / 2], name='Mean_Value')
        self.assertTrue('Mean_Value' in result.columns)  # Check if new column exists
        pd.testing.assert_series_equal(result['Mean_Value'], expected_mean_values, check_names=True)  # Check values

if __name__ == "__main__":
    unittest.main()
