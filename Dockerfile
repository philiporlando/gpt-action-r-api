# Start from a Python 3.10 base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/gpt_action_r_api

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ed \
    less \
    locales \
    vim-tiny \
    wget \
    ca-certificates \
    fonts-texgyre \
    && rm -rf /var/lib/apt/lists/*

# Configure default locale
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8

# Set environment variables
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    R_BASE_VERSION=4.2.1

# Add CRAN repository for Debian Bookworm
RUN echo "deb http://cloud.r-project.org/bin/linux/debian bookworm-cran40/" > /etc/apt/sources.list.d/cran.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys '95C0FAF38DB3CCAD0C080A7BDC78B2DDEABC47B7'

# Install R
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    r-base \
    r-base-dev \
    r-recommended \
    && rm -rf /var/lib/apt/lists/*

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
