FROM python:3.8

WORKDIR /post-service

COPY post-service/requirements.txt .
RUN pip install -r requirements.txt

COPY ./post-service/ .

CMD ["python", "post-service.py"]
