# Start from a Python 3.9 base image
FROM python:3.10

# Install R
RUN apt-get update \
    && apt-get install -y r-base \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/gpt_action_r_api

# Copy the poetry files to the working directory
COPY pyproject.toml .
COPY poetry.lock .

# Install any Python dependencies
RUN pip install --no-cache-dir poetry && poetry install

# Copy the content of the local src directory to the working directory
COPY app/ app/

# Restore R packages from renv.lock
# TODO troubleshoot renv::restore() requiring user prompt?
COPY renv.lock .
RUN Rscript -e 'install.packages("renv")'
RUN Rscript -e 'Sys.setenv(RENV_CONFIG_RESTORE_CONFIRM = FALSE); renv::restore()'

# Specify the port number the container should expose
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "-m", "app.main", "--host", "0.0.0.0", "--port", "8000"]
