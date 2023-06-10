import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'  # Replace with your desired AWS region
)

# Create an S3 client using the session
s3_client = session.client('s3')

# Create a new S3 bucket
bucket_name = 'my-bucket'
s3_client.create_bucket(Bucket=bucket_name)

# Upload a file to the bucket
file_path = 'path/to/myfile.txt'
s3_client.upload_file(file_path, bucket_name, 'myfile.txt')

# List objects in the bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])

# Delete the bucket
s3_client.delete_bucket(Bucket=bucket_name)
