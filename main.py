from google.cloud import storage
import os

def create_bucket_if_not_exists(bucket_name, project_id):
    """Creates a new bucket if it doesn't already exist."""

    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)

    if not bucket.exists():
        bucket.create()
        print(f"Bucket {bucket.name} created")
    else:
        print(f"Bucket {bucket.name} already exists")

def upload_files_to_bucket(bucket_name, project_id, source_folder):
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.get_bucket(bucket_name)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            local_file_path = os.path.join(root, file)
            blob = bucket.blob(file)
            blob.upload_from_filename(local_file_path)
            print(f"Uploaded {file} to {bucket_name}")

bucket_name = "waqasghaloo1010"
project_id = "copper-harbor-397011"  # Replace with your actual project ID
source_folder = "E:\Personal Laptop Data\Docs\Certifications\GETCERT_DE\MODULES"  # Replace with the path to your local folder

create_bucket_if_not_exists(bucket_name, project_id)
upload_files_to_bucket(bucket_name, project_id, source_folder)
