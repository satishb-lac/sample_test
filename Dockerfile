FROM jcdemo/flaskapp 

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PORT = 58080
ENTRYPOINT ["python"]
CMD ["file_copy.py"]
