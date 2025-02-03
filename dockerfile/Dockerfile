# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /home

# Install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements (Pillow for image processing)
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


