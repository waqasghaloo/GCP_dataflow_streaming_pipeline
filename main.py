from google.cloud import storage

# this code is from code cloud IDE extension, first follow instruction in API to enable, authenticate, login your
# IDE with your email which is associated with account on GCP

def create_bucket(bucket_name, project_id):
    """Creates a new bucket."""

    storage_client = storage.Client(project=project_id)

    bucket = storage_client.create_bucket(bucket_name)

    print(f"Bucket {bucket.name} created")

bucket_name = "waqasghaloo1010"
project_id = "copper-harbor-397011"  # Replace with your actual project ID

create_bucket(bucket_name, project_id)
