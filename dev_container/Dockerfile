FROM python:3.11

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Set workdir
WORKDIR /workspace/Likhit

# Copy and install Python dependencies if needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
