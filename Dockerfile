# Pull base image
FROM python:3.14.9-slim

# Install git
RUN apt-get update && \
    apt-get install -y git xmlsec1 && \
    apt-get clean

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /opt/grove

# Copy project
# This all git tracked files will be copied, so that
# the version can be derived without any git diffs
COPY --exclude=.git . .

# Temporarily mount the .git folder to infer the version during installation
RUN --mount=source=.git,target=.git,type=bind \
    pip install -e .

RUN src/manage.py collectstatic

# PORT
EXPOSE 5000

# Commands to run migration and start the server
CMD ["sh", "-c", "src/manage.py migrate && grove"]
