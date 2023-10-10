from sqlalchemy import create_engine
import pandas as pd

# Define the database connection URL here
db_url = 'postgresql+psycopg2://moc-dev:moc-dev@devqa-kpix.postgres.database.azure.com/rdm'

class DatabaseConnection:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def get_data(self, query):
        df = pd.read_sql_query(query, self.engine)
        return df
    
# Create an instance of the DatabaseConnector
db_conn = DatabaseConnection(db_url)


