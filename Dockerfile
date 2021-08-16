FROM python:3.9

WORKDIR /flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/app.py"]