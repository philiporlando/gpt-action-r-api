# Start from a Python 3.9 base image
FROM python:3.10

# Install R
RUN apt-get update \
    && apt-get install -y r-base \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY pyproject.toml .

# Install any dependencies
RUN pip install --no-cache-dir poetry && poetry install

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the port number the container should expose
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "-m", "app.main", "--host", "0.0.0.0", "--port", "8000"]
