import pandas as pd
import numpy as np
import os

import mysql.connector
from mysql.connector import Error
import warnings
warnings.filterwarnings("ignore")
import time

import logging

logging.basicConfig(
    filename= r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis\log\ingest_db.log",
    level = logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode= "a")

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', # Enter your MySQL username here
    'password': 'parshvpatel@0910', # Enter your MySQL password here
    'database': 'vender'
}

# List of CSV files and their corresponding table names
file_name = []
file_csv = []
start = time.time()
for file in os.listdir(r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis"):
    if ".csv" in file:
        file_name.append(file.split(".")[0])
        file_csv.append(file)
        df = pd.read_csv(r'C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis/' + file)

csv_files = []
for csv_file, csv_name in zip(file_name, file_csv):
        csv_files.append((csv_name, csv_file))
        
# Folder containing the CSV files 
folder_path = r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis"  # Add your folder path here

# Configuration for batch processing
BATCH_SIZE = 1000  # Process data in batches to avoid memory/connection issues
MAX_RETRIES = 3    # Number of retries for failed operations

def get_sql_type(dtype, series=None):
    """Convert pandas dtype to appropriate MySQL data type"""
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'DOUBLE' 
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:

        if series is not None:
            max_length = series.astype(str).str.len().max()
            if pd.isna(max_length) or max_length == 0:
                return 'VARCHAR(255)'
            elif max_length <= 255:
                return f'VARCHAR({min(255, max(50, int(max_length * 1.2)))})'
            else:
                return 'TEXT'
        return 'VARCHAR(255)'

def create_connection_with_retry():
    """Create database connection with retry logic"""
    for attempt in range(MAX_RETRIES):
        try:
            # Try with SSL disabled first
            config = DB_CONFIG.copy()
            config['ssl_disabled'] = True
            conn = mysql.connector.connect(**config)
            
            # Test the connection
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
            cursor.close()
            return conn
            
        except (Error, AttributeError) as e:
            logging.info(f"Connection attempt {attempt + 1} with SSL disabled failed: {e}")
            
            # Try without SSL parameters if SSL-related error
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                cursor.fetchone()
                cursor.close()
                logging.info(f"Successfully connected to MySQL database (default SSL)")
                return conn
            except Error as e2:
                logging.info(f"Connection attempt {attempt + 1} with default SSL failed: {e2}")
                
            if attempt < MAX_RETRIES - 1:
                logging.info(f"Retrying in 5 seconds...")
                time.sleep(5)
            else:
                raise Exception(f"Failed to connect after {MAX_RETRIES} attempts")

def recreate_database():
    """Drop and recreate the target database"""
    init_config = DB_CONFIG.copy()
    del init_config['database']
    
    for attempt in range(MAX_RETRIES):
        try:
            # Try with SSL disabled first
            config_with_ssl_disabled = init_config.copy()
            config_with_ssl_disabled['ssl_disabled'] = True
            
            try:
                conn = mysql.connector.connect(**config_with_ssl_disabled)
            except (Error, AttributeError):
                # If SSL disabled doesn't work, try default connection
                conn = mysql.connector.connect(**init_config)
            
            cursor = conn.cursor()
            
            # Drop database if exists and create new one
            cursor.execute(f"DROP DATABASE IF EXISTS `{DB_CONFIG['database']}`")
            cursor.execute(f"CREATE DATABASE `{DB_CONFIG['database']}`")
            
            logging.info(f"Database '{DB_CONFIG['database']}' has been recreated successfully\n")
            
            cursor.close()
            conn.close()
            return
            
        except Error as e:
            logging.info(f"Database recreation attempt {attempt + 1} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                logging.info("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                raise

def upload_csv_to_table(csv_file, table_name, folder_path):
    """Upload a single CSV file to a MySQL table with batch processing"""
    file_path = os.path.join(folder_path, csv_file)
    
    # Check if file exists
    if not os.path.exists(file_path):
        logging.info(f"Warning: File {file_path} not found. Skipping...")
        return
    
    logging.info(f"Processing {csv_file}...")
    
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        if df.empty:
            logging.info(f"Warning: {csv_file} is empty. Skipping...")
            return
        
        logging.info(f"Loaded {len(df)} rows from {csv_file}")
        
        # Replace NaN with None to handle SQL NULL
        df = df.where(pd.notnull(df), None)
        
        # Clean column names
        df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]
        
        # Create connection for this table
        conn = create_connection_with_retry()
        cursor = conn.cursor()
        
        try:
            # Generate the CREATE TABLE statement
            columns = []
            for col in df.columns:
                sql_type = get_sql_type(df[col].dtype, df[col])
                columns.append(f'`{col}` {sql_type}')
            
            create_table_query = f'CREATE TABLE `{table_name}` ({", ".join(columns)})'
            cursor.execute(create_table_query)
            logging.info(f"Created table '{table_name}'")
            
            # Prepare batch insert
            if not df.empty:
                placeholders = ', '.join(['%s'] * len(df.columns))
                columns_str = ', '.join([f'`{col}`' for col in df.columns])
                insert_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({placeholders})"
                
                # Process data in batches
                total_rows = len(df)
                rows_inserted = 0
                
                for start_idx in range(0, total_rows, BATCH_SIZE):
                    end_idx = min(start_idx + BATCH_SIZE, total_rows)
                    batch_df = df.iloc[start_idx:end_idx]
                    
                    # Convert batch to list of tuples
                    batch_data = []
                    for _, row in batch_df.iterrows():
                        values = tuple(None if pd.isna(x) else x for x in row)
                        batch_data.append(values)
                    
                    # Insert batch with retry logic
                    batch_inserted = False
                    for attempt in range(MAX_RETRIES):
                        try:
                            cursor.executemany(insert_query, batch_data)
                            conn.commit()
                            rows_inserted += len(batch_data)
                            batch_inserted = True
                            break
                        except Error as e:
                            logging.info(f"Batch insert attempt {attempt + 1} failed: {e}")
                            if attempt < MAX_RETRIES - 1:
                                cursor.close()
                                conn.close()
                                conn = create_connection_with_retry()
                                cursor = conn.cursor()
                                time.sleep(2)
                            else:
                                raise
                    
                    if not batch_inserted:
                        raise Exception(f"Failed to insert batch after {MAX_RETRIES} attempts")
                
                logging.info(f"Successfully inserted all {rows_inserted} rows into '{table_name}'")
        
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        logging.info(f"Error processing {csv_file}: {e}")
        raise

def main():
    """Main function to orchestrate the data upload process"""
    logging.info("Starting data upload process...")
    
    # Validate folder path
    if not folder_path or not os.path.exists(folder_path):
        logging.info(f"Error: Please set a valid folder_path. Current path: '{folder_path}'")
        return
    
    try:
        # Recreate the database
        logging.info("Step 1: Recreating database...")
        recreate_database()
        
        # Wait a bit for database to be fully ready
        time.sleep(2)
        
        # Process each CSV file
        logging.info("Step 2: Processing CSV files...")
        for csv_file, table_name in csv_files:
            try:
                upload_csv_to_table(csv_file, table_name, folder_path)
                logging.info(f"Completed processing {table_name}\n")
                # Small delay between tables
                time.sleep(1)
            except Exception as e:
                logging.info(f"Failed to process {csv_file}: {e}")
                # Continue with next file instead of stopping entirely
                continue
        
        logging.info("\nData upload process completed!")
        
        # Display summary
        logging.info("\n--- Database Summary ---")
        conn = create_connection_with_retry()
        cursor = conn.cursor()
        
        try:
            for _, table_name in csv_files:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`")
                    count = cursor.fetchone()[0]
                    logging.info(f"Table '{table_name}': {count:,} rows")
                except Error:
                    logging.info(f"Table '{table_name}': Not found or error occurred")
        finally:
            cursor.close()
            conn.close()
        
    except Exception as e:
        logging.info(f"Error during upload process: {e}")
        raise


def load_raw_data():
    file_name = []
    file_csv = []
    start = time.time()
    for file in os.listdir(r"C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis"):
        if ".csv" in file:
            logging.info(file)
            file_name.append(file.split(".")[0])
            file_csv.append(file)
            df = pd.read_csv(r'C:\Users\p1a2r\OneDrive\Desktop\Git Hub Projects\Vender Performance Analysis/' + file)
            logging.info(f"Ingesting {file} in db")
    
    csv_files = []
    for csv_file, csv_name in zip(file_name, file_csv):
        csv_files.append((csv_name, csv_file))
        
    main()
    end = time.time()
    total_time = (end- start)/60
    logging.info("-------------Ingestion Complete---------------")
    logging.info(f"\nTotal Time Taken: {round(total_time, 2)} minutes")

if __name__ == "__main__":
    load_raw_data()