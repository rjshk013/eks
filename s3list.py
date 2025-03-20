import boto3

def list_bucket_contents(bucket_name):
    # Create a session using your specific profile
    session = boto3.Session(profile_name='dev')
    
    # Create an S3 client using the session
    s3 = session.client('s3')
    
    # List the files in the specified S3 bucket
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        # Check if the bucket is empty or does not exist
        if 'Contents' not in response:
            print(f"The bucket {bucket_name} is empty or does not exist.")
            return
        
        # Print out the filenames in the bucket
        print(f"Files in {bucket_name}:")
        for item in response['Contents']:
            print(f"- {item['Key']} ({item['Size']} bytes)")
    except s3.exceptions.NoSuchBucket:
        print("The specified bucket does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    bucket_name = 'your_bucket_name'  # Replace 'your_bucket_name' with the name of your bucket
    list_bucket_contents(bucket_name)
