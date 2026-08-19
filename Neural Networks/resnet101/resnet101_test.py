from torchvision import models, transforms
from PIL import Image
import torch

img = Image.open("C:/Users/nikit/.spyder-py3/bobby.jpg")

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean = [0.485, 0.456, 0.406],
        std = [0.229, 0.224, 0.225]
)])

img_t = preprocess(img)

resnet = models.resnet101(pretrained=True)

batch_t = torch.unsqueeze(img_t, 0)

resnet.eval()
out = resnet(batch_t)

with open("C:/Users/nikit/.spyder-py3/imagenet_classes.txt") as f:
    labels = [line.strip() for line in f.readlines()]
    labels = labels[4:]
    
_, indices = torch.sort(out, descending = True)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

for idx in indices[0][:5]:
    print(labels[idx], percentage[idx].item())
