FROM python:3.9-slim

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install openai
RUN pip install -r requirements.txt
RUN pip install pymysql
RUN pip install python-dotenv




CMD ["python", "main.py"]
