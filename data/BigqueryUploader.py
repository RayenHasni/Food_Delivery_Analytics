from google.cloud import bigquery
from .DataGenerator import DataGenerator
import os
from dotenv import load_dotenv

load_dotenv()


class BigQueryUploader:
    """Upload data directly to BigQuery."""
    
    def __init__(self):
        self.project_id = os.getenv("GCP_PROJECT_ID")
        self.dataset_id = os.getenv("GCP_DATASET_ID")
        self.client = bigquery.Client(project=os.getenv("GCP_PROJECT_ID"))
    
    def upload_dataframe(self, df, table_id):
        """Upload a dataframe directly to BigQuery."""
        table_ref = f"{self.project_id}.{self.dataset_id}.{table_id}"
        
        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )
        
        try:
            job = self.client.load_table_from_dataframe(df, table_ref, job_config=job_config)
            job.result()
            print(f"✓ {table_id} ({len(df)} rows)")
            return True
        except Exception as e:
            print(f"✗ Error uploading {table_id}: {str(e)}")
            return False
    
    def upload(self, customers, restaurants, orders, deliveries):
        """Upload all generated dataframes to BigQuery."""
        print(f"Uploading to {self.project_id}.{self.dataset_id}...\n")
        
        results = [
            self.upload_dataframe(customers, "customers"),
            self.upload_dataframe(restaurants, "restaurants"),
            self.upload_dataframe(orders, "orders"),
            self.upload_dataframe(deliveries, "deliveries"),
        ]
        
        print(f"\n✓ Upload complete ({sum(results)}/4 successful)")
