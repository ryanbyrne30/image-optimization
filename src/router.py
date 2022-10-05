from flask import Flask, request, jsonify
from src.utils import path as pu, image as iu, aws

app = Flask(__name__)


@app.route("/upload_image", methods=["POST"])
def upload_image():
    file = request.files["file"]

    if not pu.is_file_allowed(file.filename):
        return jsonify(success=False, message="No file given.")
    if not file or not pu.is_file_allowed(file.filename):
        return jsonify(success=False, message="Invalid file.")

    temp_dir = pu.create_temp_dir()
    filename = pu.get_secure_filename(file.filename)
    filepath = pu.join([temp_dir.name, filename])
    file.save(filepath)
    converted_path = iu.convert_to_webp(filepath)
    aws_response = aws.upload_to_s3(
        converted_path, pu.get_file_from_path(converted_path)
    )
    return jsonify(success=aws_response is not None, image=aws_response)
