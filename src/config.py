import os

AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_URL = os.environ.get("AWS_URL")
AWS_BASE_FOLDER = os.environ.get("AWS_BASE_FOLDER")

EXT_WHITELIST = os.environ.get("EXT_WHITELIST")

WHITELIST = {ext.strip() for ext in EXT_WHITELIST.split(",")}
