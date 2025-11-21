# Use Python 3.10+ as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for gmpy2
RUN apt-get update && apt-get install -y \
    gcc \
    libgmp-dev \
    libmpfr-dev \
    libmpc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app:$PYTHONPATH

# Make CLI script executable
RUN chmod +x rsa_hacker_cli.py

# Set default entrypoint to CLI tool
ENTRYPOINT ["python", "rsa_hacker_cli.py"]

# Default command shows help
CMD ["--help"]
