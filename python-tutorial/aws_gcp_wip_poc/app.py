import json
from google.cloud import storage

BUCKET_NAME = "aws s3 bucket name"

def handler(event, context):
    print(f"reading list of files from GCP storage {BUCKET_NAME}")

    gcs_client = storage.Client()
    bucket = gcs_client.get_bucket(BUCKET_NAME)

    for bucket_object in bucket.list_blobs():
        print(bucket_object)

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

if __name__ == '__main__':
    handler(None, None)