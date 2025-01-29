import boto3
import json
import requests
import os

# NASA API URL
url = "https://api.nasa.gov/planetary/apod"

# AWS S3 details
bucket_name = "nasa-project-bucket"
s3_key = "nasa-data.json"

# Create an S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get API key from environment variable
    #configuration>>eniroment varialbles>>set api key
    api_key = os.getenv("NASA_API_KEY")
    
    if not api_key:
        print("NASA API key is missing.")
        return {"statusCode": 500, "body": "Missing API Key"}

    params = {"api_key": api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print("Data fetched successfully.")

        # Upload directly to S3 without writing to a file
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json.dumps(data),
            ContentType="application/json"
        )
        print(f"File uploaded successfully to {bucket_name}/{s3_key}")
        return {"statusCode": 200, "body": "Success"}
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return {"statusCode": 500, "body": "Failed to fetch data"}
    
    except Exception as e:
        print(f"Failed to upload file: {e}")
        return {"statusCode": 500, "body": "Failed to upload data"}
