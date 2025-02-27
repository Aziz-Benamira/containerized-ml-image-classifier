@echo off
echo Starting Minikube...
minikube start --driver=docker

echo Loading images into Minikube...
minikube image load web-app-service
minikube image load ml-model-service

echo Deploying application...
kubectl apply -f db-deployment.yaml
kubectl apply -f ml-service-deployment.yaml
kubectl apply -f web-app-deployment.yaml

echo Waiting for pods to be ready...
timeout /t 60 >nul
kubectl get pods

echo Getting app URL...
minikube service web-app --url

echo Done! Open the URL in your browser.
pause