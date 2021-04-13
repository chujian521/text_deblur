import torch
import torch.nn as nn
from resnet import resnet18, resnet34, resnet50, resnet101, resnet152
import os
import argparse
from model import DeblurModel
import torch.optim as optim
from PIL import Image
from torchvision import transforms
import torchvision


blur_transform = transforms.Compose([
    transforms.ToTensor()])
unblur_transform = transforms.ToPILImage()

def load_network(save_filepath,backbone):
    network = DeblurModel(backbone)
    network = torch.nn.DataParallel(network).cuda()
    if os.path.isfile(save_filepath):
        checkpoint = torch.load(save_filepath)
        network.load_state_dict(checkpoint["network"])
    return network
        
def test_network(filename,network):
    network.eval()
    blur_img = Image.open(filename).convert("RGB")
    blur_img = blur_transform(blur_img).unsqueeze(0)        
    deblur_img = network(blur_img.cuda()).cpu()
    torchvision.utils.save_image(deblur_img, "./test/deblur.png",
                    nrow=3, normalize=True, range=(0, 1), scale_each=True, pad_value=0)
    blur_img = unblur_transform(blur_img.cpu().clone().squeeze(0))
    blur_img.save("./test/blur.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_model", default="model-23.pth", type=str, help="trained model")
    parser.add_argument("--backbone", default="resnet18", type=str)
    parser.add_argument("--blurimg", default="./test/1.png", type=str, help="test file path")
    args = parser.parse_args()
    
    network = load_network(args.train_model,args.backbone)
    test_network(args.blurimg,network)

