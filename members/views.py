import boto3
import json
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def fetch_json_from_s3(request):
    # Initialize S3 client
    s3_client = boto3.client(
        's3',
        #the below content must be add in settings.py
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME
    )

    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_key = "nasa-data.json"  # Adjust based on your S3 file path

    try:
        # Fetch file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        json_content = response['Body'].read().decode('utf-8')
        data = json.loads(json_content)  # Convert to Python dictionary
        return render(request, 'nasa_data.html', {'data': data})

        #return JsonResponse(data)  # Return as JSON response
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
