# Use a suitable Python base image
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

# Install system dependencies
RUN apt-get update &&  \
    apt-get install -y \
    gdal-bin \
    libgdal-dev \
    postgresql-client \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . /app

# Set the working directory to the folder containing manage.py
WORKDIR /app/geodjango

# Run the Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]