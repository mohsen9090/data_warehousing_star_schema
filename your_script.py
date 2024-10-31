import pandas as pd
import numpy as np

# Define a function to process a sample data
def process_data(file_path):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path)
    
    # Perform a simple operation, e.g., calculating the mean of a column
    data['Mean_Value'] = data.mean(axis=1)
    
    # Print the first few rows of the DataFrame
    print(data.head())
    
    # Return the processed DataFrame
    return data

# Example usage
if __name__ == "__main__":
    file_path = "sample_data.csv"  # Replace with your actual CSV file path
    processed_data = process_data(file_path)
