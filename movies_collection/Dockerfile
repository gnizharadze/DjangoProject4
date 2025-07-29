
FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # Add packages needed for database drivers, image processing, etc.
        # For Pillow (image processing), you'll need libjpeg-dev and zlib1g-dev.
        libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Expose the port the application runs on
EXPOSE 8000

# Run the command to start the server
# This will be overridden by docker-compose, but it's good practice to have a default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]