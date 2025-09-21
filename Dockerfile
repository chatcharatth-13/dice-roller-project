# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# Explicitly state the destination is the current directory './'
COPY . ./

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
# Use gunicorn for a production-ready server
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]