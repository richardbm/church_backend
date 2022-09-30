FROM python:3-alpine

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev
RUN apk add jpeg-dev zlib-dev libjpeg && pip install Pillow==7.2.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN mv wait-for /bin/wait-for

RUN pip install --no-cache-dir -r requirements.txt
RUN ["chmod", "+x", "/bin/wait-for"]
# Remove dependencies only required for psycopg2 build
RUN apk del .build-deps

EXPOSE 8000

CMD ["gunicorn", "church_project.wsgi", "0:8000"]