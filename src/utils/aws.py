from src import config
import boto3


def upload_to_s3(image: str, key: str) -> str:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    )
    key = f"{config.AWS_BASE_FOLDER}/{key}"
    response = s3.upload_file(image, config.AWS_BUCKET_NAME, key)
    print("AWS response", response, response is None)
    return f"{config.AWS_URL}/{key}" if response is None else None
