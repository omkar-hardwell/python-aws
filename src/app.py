"""Application setup."""
import boto3
import configs

from flask import Flask, render_template, request


# Application instance
app = Flask(configs.APP_NAME)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        # Upload file to s3 bucket
        file = request.files['fileToUpload']
        print(file.filename)
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket.name)
