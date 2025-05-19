# Use a slim Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install required system packages (fonts) and Python dependencies
RUN apt-get update && apt-get install -y \
    fonts-dejavu-core \
    && pip install --no-cache-dir flask praw pillow \
    && apt-get clean

# Expose the Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]
