FROM python:3.6

WORKDIR /app

COPY requirements.txt /app/.

RUN pip install -r requirements.txt

COPY . /app/.

ENV FLASK_RUN_PORT 58081
ENV KEY_FILE ''

ENTRYPOINT ["python"]
CMD ["vaccines_file_upload.py", "${KEY_FILE}"]
EXPOSE 58081
