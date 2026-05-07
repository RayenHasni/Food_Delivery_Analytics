from datetime import datetime
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def upload_to_bigquery():
    from data.BigqueryUploader import BigQueryUploader
    from data.DataGenerator import DataGenerator

    gen = DataGenerator(customers=14400, restaurants=4770, orders=255860)
    customers, restaurants, orders, deliveries = gen.generate_all()

    uploader = BigQueryUploader()
    uploader.upload(customers, restaurants, orders, deliveries)

default_args = {
    "start_date": datetime(2022, 1, 1),
}

with DAG(
    dag_id="food_delivery_pipeline",
    default_args=default_args,
    schedule="*/5 * * * *",
    catchup=False,
) as dag:

    bq_uploader = PythonOperator(
        task_id="generate_and_upload_data",
        python_callable=upload_to_bigquery,
    )

    dbt_build = BashOperator(
        task_id="run_dbt_build",
        bash_command="dbt build --project-dir /home/rayen_63/FoodDeliveryAnalytics/dbt",
    )

    bq_uploader >> dbt_build