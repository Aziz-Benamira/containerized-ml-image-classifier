# Use an official Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the MobileNetV3 weights
RUN python -c "import torchvision.models as models; \
               model = models.mobilenet_v3_small(weights='MobileNet_V3_Small_Weights.IMAGENET1K_V1'); \
               model.eval()"
               
# Copy your prediction script and any required files
COPY predict.py .
COPY imagenet_classes.json .  

# Set the default command to run your script
CMD ["python", "predict.py"]