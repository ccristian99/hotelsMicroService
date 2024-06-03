# Use a base Python image
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Expose the port on which the application will run
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 hotelsMicroService.wsgi:application"]

