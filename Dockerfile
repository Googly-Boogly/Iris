FROM python:3.9-slim


WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

CMD ["python", "./code/main.py"]
