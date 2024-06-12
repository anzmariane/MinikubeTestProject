FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY app.py /usr/src/app

CMD ["python", "app.py"]