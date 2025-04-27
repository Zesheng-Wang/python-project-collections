import torch

from torchvision import models, transforms

from PIL import Image

import requests

# 1. 加载预训练模型

model = models.resnet18(pretrained=True)

model.eval()

# 2. 准备ImageNet类别标签
with open("imagenet_classes.txt", "r", encoding="utf-8") as f:
    classes = [line.strip() for line in f.readlines()]
# 3. 定义图像预处理步骤

preprocess = transforms.Compose([

    transforms.Resize(256), 

    transforms.CenterCrop(224), 

    transforms.ToTensor(),

    transforms.Normalize(mean=[0.485, 0.456, 0.406],

                         std=[0.229, 0.224, 0.225])

])

# 4. 读取和预处理输入图片

img_path = "test.jpg"   # 替换成你的图片路径

img = Image.open(img_path).convert("RGB")

input_tensor = preprocess(img).unsqueeze(0)

# 5. 模型推理，获取前5个预测类别

with torch.no_grad():

    outputs = model(input_tensor)

    _, indices = torch.topk(outputs, 5)

    print("模型预测前5个类别：")

    for idx in indices[0]:

        print(classes[idx])