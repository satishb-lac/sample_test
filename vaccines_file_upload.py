from flask import Flask
from google.cloud import storage
import os,time
import logging,traceback,sys
file_path=f"data/testfile.csv"
new_blob_name=f"data/copy_sftp_file.csv"
bucket_name=os.getenv('BUCKET_NAME')

app = Flask(__name__)
@app.route("/")
def vaccines_file_upload():
    return "File uploaded "

if __name__ == "__main__":
    s=os.getenv('KEY_FILE')
    with open('cred/auth_file.json','w') as f:
        f.writelines(s)
        f.writelines('\n')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cred/auth_file.json"
    client=storage.Client()
    try:
        bucket=client.get_bucket(bucket_name)
        source_blob=bucket.blob(f"{file_path}")
        bucket.copy_blob(source_blob,bucket,new_blob_name)
        print("File copied")
        app.run(debug=True,host = '0.0.0.0',port='58081')
        app.stop()
        
    except Exception as exp:
        traceback.print_exc(limit=1,file=sys.stdout)
