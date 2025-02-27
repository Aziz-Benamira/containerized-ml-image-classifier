from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json
import io

app = Flask(__name__)

# Load the pre-trained MobileNetV3 model
model = models.mobilenet_v3_small(weights='MobileNet_V3_Small_Weights.IMAGENET1K_V1')
model.eval()

# Preprocessing steps
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def classify_image(image_file):
    img = Image.open(image_file).convert('RGB')
    
    img_tensor = preprocess(img)
    img_tensor = img_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(img_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
    with open('imagenet_classes.json') as f:
        labels = json.load(f)
    top3_prob, top3_catid = torch.topk(probabilities, 3)
    top3 = [(labels[str(catid.item())], prob.item()) for catid, prob in zip(top3_catid, top3_prob)]
    return top3

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Process the image directly from the file stream
    predictions = classify_image(file)
    return jsonify({"predictions": [{"label": label, "probability": prob} for label, prob in predictions]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)