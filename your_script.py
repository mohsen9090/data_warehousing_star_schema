import pandas as pd import numpy as np
# نمونه اسکریپت برای 
# پردازش داده‌ها
def main():
    # بارگذاری داده‌ها از 
    # یک فایل CSV
    df = pd.read_csv('data.csv') 
    print("اطلاعات اولیه:") 
    print(df.head())
    # انجام برخی عملیات 
    # پردازشی
    df['new_column'] = 
    np.log(df['existing_column'] + 1) 
    print("داده‌های پردازش 
    شده:") print(df.head())
if __name__ == "__main__":
    main()
