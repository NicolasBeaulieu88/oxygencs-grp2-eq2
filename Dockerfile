# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Set environment variables
ENV PIP_DEFAULT_TIMEOUT=100 \
# Allow statements and log messages to immediately appear
 PYTHONUNBUFFERED=1 \
# disable a pip version check to reduce run-time & log-spam
 PIP_DISABLE_PIP_VERSION_CHECK=1 \
# cache is useless in docker image, so disable to reduce image size
 PIP_NO_CACHE_DIR=1


ENV HOST=http://159.203.50.162 \ 
 TOKEN=e7026c64578833bfc1ba \
 T_MAX=20 \
 T_MIN=10 \
 DATABASE_URL=157.230.69.113 \
 DATABASE_USER=user02eq2 \
 DATABASE_PASSWORD=Dw2OtjzSOKoZvrGN \
 DATABASE_NAME=db02eq2

# Add Pipfiles
COPY Pipfile Pipfile.lock /app/

# Install pipenv and install dependencies
RUN pip install --no-cache-dir pipenv && pipenv install --deploy

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /app

# Run the command to start your application
CMD ["pipenv", "run", "python", "src/main.py"]