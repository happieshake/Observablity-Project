# Use official Python lightweight image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our application code
COPY app.py .

# Tell Docker our app uses port 5000
EXPOSE 5000

# The command to run our application
CMD ["python", "app.py"]