from google.cloud import bigquery
import pandas as pd

def upload_to_bigquery(dataset_id, table_id, dataframe):
    # ایجاد یک کلاینت BigQuery
    client = bigquery.Client()

    # تعریف جدول مقصد
    table_ref = client.dataset(dataset_id).table(table_id)

    # بارگذاری داده‌ها به BigQuery
    job = client.load_table_from_dataframe(dataframe, table_ref)

    job.result()  # منتظر تمام شدن بارگذاری

    print(f"Loaded {job.output_rows} rows into {dataset_id}:{table_id}.")

if __name__ == "__main__":
    # مسیر فایل CSV که از Excel پردازش شده است
    file_path = "processed_data.csv"  # به مسیر فایل خود اشاره کنید

    # خواندن داده‌ها از فایل CSV
    df = pd.read_csv(file_path)

    # بارگذاری داده‌ها به BigQuery
    dataset_id = 'your_dataset_id'  # شناسه دیتاست خود را وارد کنید
    table_id = 'your_table_id'  # شناسه جدول خود را وارد کنید
    upload_to_bigquery(dataset_id, table_id, df)
