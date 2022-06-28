FROM python:3.10.4-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_EMAIL admin@gmail.com

# Set work directory
WORKDIR /BasicApp

# Install dependencies
COPY requirements.txt /BasicApp/

RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /BasicApp/

CMD python manage.py makemigrations --no-input && \
    python manage.py migrate --no-input && \
    python manage.py collectstatic --no-input; \
    python manage.py createsuperuser --no-input; \
    python manage.py runserver 0.0.0.0:8000
