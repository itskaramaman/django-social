FROM python:3.10-alpine3.17

ENV PYTHONBUFFERED 1

RUN apk update && apk add --no-cache postgresql-dev musl-dev gcc python3-dev

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]