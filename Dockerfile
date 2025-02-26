# Use an official PyTorch base image (CPU version for simplicity)
FROM pytorch/pytorch:1.13.0-cpu

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your prediction script and any required files
COPY predict.py .
COPY imagenet_classes.json . 
# Set the default command to run your script
CMD ["python", "predict.py"] 