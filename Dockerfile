FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set up app directory
WORKDIR /app

# Copy and install requirements
COPY . /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt || true

# Default command
CMD ["python3", "main.py"]
