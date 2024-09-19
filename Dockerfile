# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and coreutils (which includes the date command)
RUN apt-get update && apt-get install -y coreutils && pip install --no-cache-dir flask

# Expose port 5000 (Flask's default port)
EXPOSE 5000

# Define the command to run your app using Python
CMD ["python", "app.py"]
