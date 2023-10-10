# data_functions.py

import pandas as pd
import tempfile
from db_connection import db_conn

def get_data():
    query = """SELECT * FROM moc_org.customer LIMIT 3;"""
    df = db_conn.get_data(query)
    return df

def create_temp_csv(data):
    temp_dir = tempfile.mkdtemp()
    csv_file_path = f"{temp_dir}/temp_data.csv"
    data.to_csv(csv_file_path, index=False)
    return csv_file_path
