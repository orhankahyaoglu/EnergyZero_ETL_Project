from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import subprocess

# 1️⃣ Default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 2️⃣ DAG tanımı
dag = DAG(
    'energyzero_etl',
    default_args=default_args,
    description='EnergyZero veri ETL pipeline',
    schedule_interval='0 1 * * *',  # her gün sabah 6'da çalışır
    start_date=datetime(2025, 10, 25),
    catchup=False,
)

# 3️⃣ Python fonksiyonları
def extract_data():
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/extract_energyzero.py')
    subprocess.run(['python', script_path], check=True)

def transform_data():
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/transform_pandas.py')
    subprocess.run(['python', script_path], check=True)
    
def visualize_data():
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/hourly_boxplot.py')
    subprocess.run(['python', script_path], check=True)


# 4️⃣ Airflow task'ları
extract_task = PythonOperator(
    task_id='extract_energyzero',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_pandas',
    python_callable=transform_data,
    dag=dag
)

visualize_task = PythonOperator(
    task_id='generate_hourly_boxplot',
    python_callable=visualize_data,
    dag=dag
)

# 5️⃣ Task sırası
extract_task >> transform_task >> visualize_task

