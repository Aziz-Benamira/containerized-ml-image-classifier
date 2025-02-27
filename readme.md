# Containerized ML Image Classifier

A machine learning application for image classification using MobileNetV3, containerized with Docker and orchestrated with Kubernetes.

## Features
- Upload images via a Flask web app.
- Classify images with a PyTorch-based ML service.
- Store results in PostgreSQL.
- View classification history.
- Deployed on Kubernetes with Minikube.

## Project Structure
- `web-app/`: Flask web application.
- `ml-service/`: ML model service (assumed in root for simplicity).
- `k8s/`: Kubernetes manifests.
- `docker-compose.yml`: Local testing setup.

## Running Locally with Docker Compose
cd C:\Users\benam\Downloads\containerized-ml-image-classifier\k8s
start-app.bat