FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN groupadd --system django && useradd --system --gid django django

# Install dependencies
RUN apt-get update \
    && apt-get install -y build-essential gcc libcairo2 libffi-dev \
    libgdk-pixbuf2.0-0 libpango-1.0-0 libpangocairo-1.0-0 poppler-utils \
    python3-cffi shared-mime-info \
    libpq-dev python3-dev \
    file\
    && rm -rf /var/lib/apt/lists/*

# Install pip packages
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --upgrade supervisor

WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt

# Create the static_backend volume as a directory
RUN mkdir -p /static_backend \
    && chown -R django:django /static_backend \
    && chmod -R o+r /static_backend

# Create the supervisor configuration files volume as a directory
RUN mkdir -p /supervisor.d \
    && chown -R django:django /supervisor.d \
    && chmod -R o+r /supervisor.d

# Create the web server logs volume as a directory
RUN mkdir -p /web_server_logs/supervisord_logs  \
    && mkdir -p /web_server_logs/gunicorn_logs \
    && mkdir -p /web_server_logs/server_logs \
    && chown -R django:django /web_server_logs \
    && chmod -R o+r /web_server_logs

# Create the history volume as a directory
RUN mkdir -p /.history \
    && chown -R django:django /.history \
    && chmod -R o+r /.history

# Change the directories into volumes
VOLUME /web_server_logs /supervisor.d /.history /static_backend
# Copy the supervisord.conf file over to the container
COPY ./supervisord.conf ./supervisord.conf

# Copy the gunicorn_config.py file over to the container
COPY ./gunicorn_config.py ./gunicorn_config.py

# Define environment variables
ENV PYTHONPATH="/app"
ENV HISTFILE="/.history/.bash_history"
ENV IPYTHONDIR="/.history/.ipython/"

# Add some terminal jazz
RUN echo "PS1='docker@\$NAME:\w\$ '" >> /etc/bash.bashrc

WORKDIR /app
