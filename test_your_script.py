 import unittest
from unittest.mock import patch
import pandas as pd
from your_script import process_data

class TestYourScript(unittest.TestCase):

    @patch('your_script.pd.read_csv')
    def test_example(self, mock_read_csv):
        # Mock کردن DataFrame که توسط pd.read_csv بازگردانده می‌شود
        mock_data = pd.DataFrame({
            'Column1': [1, 2, 3],
            'Column2': [4, 5, 6],
        })
        mock_read_csv.return_value = mock_data

        # تعریف مسیر فایل
        file_path = "sample_data.csv"  
        result = process_data(file_path)  # فراخوانی تابع با مسیر فایل

        # بررسی صحت محاسبه ستون 'Mean_Value'
        expected_mean_values = pd.Series([(1 + 4) / 2, (2 + 5) / 2, (3 + 6) / 2])
        self.assertTrue('Mean_Value' in result.columns)  # بررسی وجود ستون جدید
        pd.testing.assert_series_equal(result['Mean_Value'], expected_mean_values)  # بررسی مقادیر

if __name__ == "__main__":
    unittest.main()
