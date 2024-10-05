from flask import Flask, request
import json
import os
import boto3

app = Flask(__name__)
s3_client = boto3.client('s3')

@app.route("/")
def hello_world():
    return "hello"

@app.route("/path/<string:p>")
def hello_p(p):
    return f"echo {p}"

@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method != 'POST':
        return "get request"
    return request.json["msg"]

@app.route("/dl", methods=['POST'])
def dl():
    file = request.files.get('file')
    file_name = "uploaded_" + file.filename
    file_path = os.path.join('files', file_name)
    file.save(file_path)
    return "saved"

@app.route("/s3", methods=['POST'])
def s3_upload():
    file = request.files.get('file')
    file_name = "uploaded_" + file.filename
    file_path = os.path.join('files', file_name)
    s3_client.upload_fileobj(file.stream, "bucket", file_path)
    return "s3 uploaded"

