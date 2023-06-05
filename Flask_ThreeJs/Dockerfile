# Base image with Python and Node.js
FROM python:3.9-slim-buster as base

# Install Node.js and npm
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Set the working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy and install Node.js dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the frontend assets
RUN npm run build

# Expose the port on which the application runs
EXPOSE 5000

# Set the entry point command
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]



