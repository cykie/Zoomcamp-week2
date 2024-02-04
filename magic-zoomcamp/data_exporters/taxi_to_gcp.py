from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="/home/src/magic-zoomcamp/zmcp-413216-76fb4b30e421.json"
bucket_name='mage-zmcp'
project_id='zmcp-413216'
table_name='green_taxi'
root_path= f'{bucket_name}/{table_name}'
object_key = 'green_taxi_data.parquet'


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:

    
    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
