# 🚀 Project Completed: NASA API Data Extraction and Display Using AWS, EventBridge, S3 & Django 🌌

![nasa_etl_pipline drawio](https://github.com/user-attachments/assets/719ca71a-cc56-44b2-98a3-48a059f78fcb)


I’m thrilled to share a project that I’ve recently completed where I integrated several powerful technologies to automate data extraction and visualization. The goal of this project was to create a seamless system for fetching NASA’s Astronomy Picture of the Day (APOD) and displaying it on a web page. Here’s a breakdown of the key components and how they work together:

# 🔧 Tech Stack:
-AWS Lambda: A serverless computing service that fetches the data from NASA's API and processes it.
Amazon S3: A scalable cloud storage service to store the fetched JSON data.
AWS EventBridge: A serverless event bus that triggers the Lambda function at regular intervals (once a day).
Django: A high-level Python web framework used to build a simple web app that displays the fetched data.
boto3: The AWS SDK for Python, used to interact with AWS services like Lambda and S3.
# 💡 How the Project Works:
NASA API Data Fetching:
I set up an AWS Lambda function to fetch data from NASA’s Astronomy Picture of the Day (APOD) API. The data includes details like the title, explanation, image URL, and other metadata.
The Lambda function retrieves the data in JSON format and stores it in an S3 bucket.
Automated Data Fetching with EventBridge:

To ensure that the data is updated automatically, I used AWS EventBridge to trigger the Lambda function at a scheduled time (daily).
This ensures that new data is fetched every day without manual intervention.
Data Storage in S3:

The JSON response from the NASA API is stored in an Amazon S3 bucket. This makes it easy to access and use the data later for web display.
The data is stored as a JSON file (nasa-data.json), which contains the date, title, explanation, and image URL for the APOD.
Django Web Application:

On the frontend, I built a Django web app that fetches and displays the data stored in the S3 bucket.
Using boto3, the Django app retrieves the JSON file from the S3 bucket and parses the data into a human-readable format on the webpage.
The webpage is designed to display:
The title of the image.
A brief description or explanation of the image.
The image itself in high definition (HD URL).
The app provides a simple, elegant user interface that allows users to view the NASA data in real-time.

![127 0 0 1_8000_nasa_json_ (3)](https://github.com/user-attachments/assets/e9caa7b7-8337-441d-b454-dbec1ea94029)


# ⚙️ Detailed Workflow:
Data Extraction (Lambda):

Lambda makes an HTTP request to NASA’s API and retrieves the data in JSON format.
The extracted data is then saved to an S3 bucket, allowing it to be accessible at any time.
Event Automation (EventBridge):

EventBridge ensures that the Lambda function runs at regular intervals (e.g., once every 24 hours).
This eliminates the need for manual intervention and ensures the data stays up-to-date.
Web Interface (Django):

The Django app fetches the latest JSON data from the S3 bucket using boto3.
The data is parsed and displayed on a user-friendly web page using HTML/CSS.
Users can view the APOD image, read the description, and explore more about the day's featured content.

# 🌟 Key Benefits:

Automation: The data is fetched and updated automatically every day via EventBridge and Lambda. This allows for hands-off operation once set up.
Scalability: With AWS, the entire system can scale based on demand. Both Lambda and EventBridge handle large amounts of requests effortlessly.
Cost-Effective: Using AWS Lambda and S3 ensures that I only pay for the resources I use, making the solution cost-effective for small to medium-sized applications.
Seamless Integration: By using boto3, I was able to easily integrate AWS services (Lambda, S3, EventBridge) into my Django web app.
User-Friendly Display: Django’s flexibility allowed me to create a clean, responsive webpage where users can easily read and view the NASA data.


