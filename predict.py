import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json

# Load the pre-trained MobileNetV3 model
model = models.mobilenet_v3_small(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Define the image preprocessing steps
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to classify the image
def classify_image(img_path):
    # Load and preprocess the image
    img = Image.open(img_path)
    img_tensor = preprocess(img)
    img_tensor = img_tensor.unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(img_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # Load ImageNet class labels
    with open('imagenet_classes.json') as f:
        labels = json.load(f)

    # Get top 3 predictions
    top3_prob, top3_catid = torch.topk(probabilities, 3)
    top3 = [(labels[str(catid.item())], prob.item()) for catid, prob in zip(top3_catid, top3_prob)]

    return top3

if __name__ == "__main__":
    # For testing
    result = classify_image('path/to/test/image.jpg')
    print(result)