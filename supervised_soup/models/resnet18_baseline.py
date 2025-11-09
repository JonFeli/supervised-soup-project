"""
Purpose:
    Build and test a "bare" (untrained) ResNet-18 model 
    to verify that the architecture and output dimensions are correct.

Description:
    This script creates a ResNet-18 model without pretrained weights (weights=None),
    replaces the final fully connected (fc) layer with a linear layer that outputs 
    predictions for 10 classes, transfers the model to the available device 
    (GPU if available, otherwise CPU), and performs one forward pass on 
    a batch of randomly generated data.

Outcome:
    The script will print the shape of the output tensor (expected: [2, 10]),
    which means: batch of 2 images → 10 logits (one per class).
    
"""

import torch
from torchvision import models

# Select device: GPU if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"


# Build the model
# Load ResNet-18 architecture with random (non-pretrained) weights.
# By default, ResNet-18 has 1000 output classes (ImageNet),
# so we replace the final fully connected layer with a new one for 10 classes.
model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 10)

# Move the model to the selected device and set it to evaluation mode
model = model.to(device)
model.eval()

# Test the model
# Create a fake batch of images with shape (2, 3, 224, 224):
#   "2" is a batch size (two images)
#   "3" is a number of color channels (RGB)
#   "224x224" is a standard ResNet input size
x = torch.randn(2, 3, 224, 224, device=device)

# Perform a forward pass (no gradient computation needed)
with torch.no_grad():
    logits = model(x)

# Output verification
# Print the shape of the output tensor.
# Expected: [2, 10] — one vector of 10 predictions for each of the 2 input images.
print("Output shape:", logits.shape)  
