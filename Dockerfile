
FROM python:3.9-slim

# Install dependencies
RUN pip install flask requests

# Copy application files
COPY . /app

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
