# Use official Python lightweight image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# skipping caching packages to reduce image size 

# Copy our application code to the current working directory 
COPY app.py .

# Tell Docker our app uses port 5005 applications uses 5005 ref app.py
EXPOSE 5225

# The command to run our application
CMD ["python", "app.py"]