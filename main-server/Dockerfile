FROM python:3.9

WORKDIR /main-server

COPY main-server/requirements.txt .

RUN pip install -r requirements.txt

COPY ./main-server/ .

CMD ["python", "server.py"]