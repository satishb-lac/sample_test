from flask import Flask
from google.cloud import storage
import os,time
file_path = f"data/sftp_file.csv"
bucket_name=os.getenv('BUCKET_NAME')
print(bucket_name)


app = Flask(__name__)
@app.route("/")
def file_copy():
    return "File uploaded "


#ita-electedoffice-vaccines-temp
def upload_to_gcs(file):
    s = os.getenv('KEY_FILE')
    with open('cred/gcloud.json','w') as f:
        f.writelines(s)
        f.writelines('\n')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cred/gcloud.json"
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(f"{file_path}")
    blob.upload_from_filename(file)


if __name__ == "__main__":
    file = "data/sample_file.csv"
    try:
        upload_to_gcs(file)
        app.run(debug=True,host = '0.0.0.0',port='58081')
    except Exception as exp:
        print(exp)
