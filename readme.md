# Containerized ML Image Classifier

A cutting-edge machine learning application that classifies images using MobileNetV3, packaged with Docker for seamless containerization and orchestrated with Kubernetes for robust deployment. This project showcases a full-stack ML pipeline—from model inference to a user-friendly web interface—built with modern DevOps practices.

![Demo Screenshot](https://via.placeholder.com/800x400.png?text=Demo+Screenshot) <!-- Replace with actual screenshot link -->

## Overview

This project leverages PyTorch, Flask, PostgreSQL, Docker, and Kubernetes to deliver an end-to-end image classification experience. Users can upload images through a sleek web interface, receive real-time predictions from a pre-trained ML model, and explore their classification history—all backed by a scalable, containerized architecture.

### Key Features
- **Image Upload & Classification**: Upload any image via a responsive Flask web app and get instant predictions powered by MobileNetV3.
- **ML Inference Service**: A dedicated PyTorch-based REST API service for classifying images with top-3 predictions.
- **Persistent Storage**: Stores classification results and image metadata in PostgreSQL for historical tracking.
- **Interactive History**: View past classifications with a dynamic, styled table interface.
- **Containerized Deployment**: Fully containerized with Docker for consistency across environments.
- **Kubernetes Orchestration**: Deployed locally with Minikube, featuring scalability, persistence, and service discovery.

## Tech Stack
- **Machine Learning**: PyTorch, MobileNetV3
- **Web Framework**: Flask (REST API and UI)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube)
- **Frontend**: HTML, CSS (custom styling), JavaScript (basic dynamism)
- **Tools**: Minikube, kubectl, Docker Compose

## Project Structure
```
/containerized-ml-image-classifier
├── web-app/                # Flask web application
│   ├── Dockerfile         # Docker config for web app
│   ├── app.py             # Main Flask app with UI and API integration
│   ├── requirements.txt   # Python dependencies
│   ├── templates/         # HTML templates with custom CSS
│   └── uploads/           # Local storage for uploaded images
├── Ml-model/            # ML inference service 
│   ├── Dockerfile         # Docker config for ML service
│   ├── ml_app.py          # Flask API for image classification
│   ├── requirements.txt   # Python dependencies
│   └── imagenet_classes.json # Labels for MobileNetV3
├── k8s/                   # Kubernetes manifests
│   ├── db-deployment.yaml # PostgreSQL deployment and service
│   ├── ml-service-deployment.yaml # ML service deployment and service
│   ├── web-app-deployment.yaml # Web app deployment and service
│   └── start-app.bat      # Script to restart app locally
├── docker-compose.yml     # Local multi-container setup with Docker Compose
└── README.md              # Project documentation
```

## Getting Started

### Prerequisites
- **Docker Desktop**: For containerization and Minikube’s Docker driver.
- **Minikube**: Local Kubernetes cluster.
- **kubectl**: Kubernetes CLI.
- Windows (assumed from paths; adaptable to other OS).

### Running Locally with Docker Compose
For quick testing without Kubernetes:
1. Navigate to the project root:
  
2. Start the app:
   ```bash
   docker-compose up --build
   ```
3. Access at `http://localhost:5000` in your browser.

### Running on Kubernetes (Local)
For a production-like setup with Minikube:
1. Start Minikube:
   ```bash
   minikube start --driver=docker
   ```
2. Load local Docker images:
   ```bash
   minikube image load web-app-service
   minikube image load ml-model-service
   ```
3. Deploy to Kubernetes:
   ```bash
   cd k8s
   kubectl apply -f db-deployment.yaml
   kubectl apply -f ml-service-deployment.yaml
   kubectl apply -f web-app-deployment.yaml
   ```
4. Get the app URL:
   ```bash
   minikube service web-app --url
   ```
5. Open the URL (e.g., `http://192.168.49.2:30000`) in your browser.

#### Restarting After Shutdown
Use the provided script:
```bash
cd C:\Users\benam\Downloads\containerized-ml-image-classifier\k8s
.\start-app.bat
```
- Starts Minikube, loads images, and provides the URL without redeploying (assuming cluster state persists).

## How It Works
1. **User Interaction**: Upload an image via the web app’s stylish interface.
2. **REST API**: The web app sends the image to the ML service’s `/classify` endpoint.
3. **ML Inference**: MobileNetV3 processes the image and returns top-3 predictions as JSON.
4. **Data Storage**: Results are saved to PostgreSQL with persistent volumes.
5. **History View**: Browse past classifications in a dynamic table.

## Skills Demonstrated
- **Machine Learning**: Integrated a pre-trained PyTorch model for image classification.
- **Backend Development**: Built RESTful APIs with Flask for seamless component integration.
- **Frontend Development**: Crafted a responsive UI with custom CSS and JavaScript.
- **DevOps**: Containerized with Docker and orchestrated with Kubernetes for scalability and resilience.
- **Database Management**: Leveraged PostgreSQL for persistent data storage.

## Future Enhancements
- Deploy to a cloud provider (e.g., GKE) for public access.
- Add user authentication for personalized history.
- Implement real-time prediction updates with WebSockets.
- Enhance UI with advanced JavaScript frameworks (e.g., React).

## Demo
- **Local Demo**: Run with `start-app.bat` and record a video (portfolio-ready).


---

*Created by Aziz Ben Amira – A showcase of ML, DevOps, and full-stack skills.*


