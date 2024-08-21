FROM python:3.10-slim

EXPOSE 8000

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

ENV DJANGO_SETTINGS_MODULE=csproject.settings

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
