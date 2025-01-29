import json
import psycopg2  # For PostgreSQL, use mysql.connector for MySQL
import boto3
import os

# RDS connection details
rds_host = os.environ['RDS_HOST']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

# S3 bucket name and file key
s3_client = boto3.client('s3')

def create_table(cursor):
    # SQL to create the table (if not already exists)
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS nasa_data (
        id SERIAL PRIMARY KEY,
        date DATE,
        explanation TEXT,
        hdurl TEXT,
        media_type VARCHAR(20),
        service_version VARCHAR(20),
        title VARCHAR(255),
        url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(create_table_sql)

def insert_data(cursor, data):
    # Insert the JSON data into the RDS table
    insert_sql = """
    INSERT INTO nasa_data (date, explanation, hdurl, media_type, service_version, title, url)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for item in data:
        cursor.execute(insert_sql, (
            item['date'],
            item['explanation'],
            item['hdurl'],
            item['media_type'],
            item['service_version'],
            item['title'],
            item['url']
        ))

def lambda_handler(event, context):
    try:
        # Extract S3 bucket name and file key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        print(bucket_name,file_key)

        # Download the file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        json_data = json.loads(response['Body'].read().decode('utf-8'))  # Read and parse JSON data
        print(json_data)
        
        # Connect to RDS PostgreSQL/MySQL
        conn = psycopg2.connect(
            host=rds_host,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        create_table(cursor)

        # Insert data into the RDS table
        insert_data(cursor, json_data)

        # Commit the transaction
        conn.commit()

        cursor.close()
        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps('Data successfully inserted into RDS.')
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to insert data into RDS.')
        }

