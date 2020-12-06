FROM python:3.8-alpine

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

EXPOSE 8080

COPY /src /app

WORKDIR /app

ENTRYPOINT ["gunicorn", "--config", "gunicorn.py", "main:app", "--access-logfile", "-", "--error-logfile", "-"]


