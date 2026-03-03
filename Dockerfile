# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements from the root directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the specific project folder
COPY plaud-integration/ ./plaud-integration/

# Expose the port the app runs on
EXPOSE 5001

# Command to run the receiver
CMD ["python", "plaud-integration/receiver.py"]
