import pandas as pd

def process_excel(file_path):
    # خواندن داده‌ها از فایل Excel
    data = pd.read_excel(file_path, engine='openpyxl')

    # انجام محاسبات اولیه یا تمیز کردن داده‌ها
    # به عنوان مثال، حذف مقادیر گمشده
    data = data.dropna()

    # نمایش اطلاعات اولیه
    print(data.head())

    # بازگرداندن DataFrame پردازش شده
    return data

if __name__ == "__main__":
    file_path = "path_to_your_excel_file.xlsx"  # مسیر فایل Excel
    processed_data = process_excel(file_path)
