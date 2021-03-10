import torch
import torch.nn as nn
from resnet import resnet18, resnet34, resnet50, resnet101, resnet152
import os
from model import DeblurModel
import torch.optim as optim
from PIL import Image
from torchvision import transforms
import torchvision
import easyocr
import difflib

blur_transform = transforms.Compose([
    transforms.ToTensor()])
unblur_transform = transforms.ToPILImage()

def load_network():
    network = DeblurModel("resnet18")
    network = torch.nn.DataParallel(network).cuda()
    save_filepath = "./model-91.pth"
    if os.path.isfile(save_filepath):
        checkpoint = torch.load(save_filepath)
        network.load_state_dict(checkpoint["network"])
    return network
        
def test_network(filename,network):
    network.eval()
    blur_img = Image.open(filename).convert("RGB")
    blur_img = blur_transform(blur_img).unsqueeze(0)        
    deblur_img = network(blur_img.cuda()).cpu()
    torchvision.utils.save_image(deblur_img, "./test/deblur0.png",
                    nrow=3, normalize=True, range=(0, 1), scale_each=True, pad_value=0)
    blur_img = unblur_transform(blur_img.cpu().clone().squeeze(0))
    blur_img.save("./test/blur.png")

if __name__ == "__main__":
    ratio = 0.0
    network = load_network()
    reader = easyocr.Reader(['ch_sim']) 
    for name in range(1,1000):
        flag = True
        image_id = '{0:07d}'.format(name)
        orig_image_path = "./data/%s_orig.png" % image_id
        deblur_image_path = "./data/%s_deblur.png" % image_id
        test_network(deblur_image_path, network)
        ocr_orig = reader.readtext(orig_image_path)[0][1]
        try:
            #ocr_blur = reader.readtext(deblur_image_path)[0][1]
            ocr_deblur = reader.readtext('./test/deblur0.png')[0][1]
        except Exception as e:
            flag = False
            print(e)
            
        if(flag):
            correct_ratio = difflib.SequenceMatcher(None, ocr_orig, ocr_deblur).quick_ratio()
        else:
            correct_ratio = 0.0
            ocr_blur = " "
        print(str(ocr_orig)+" " + str(ocr_deblur)+ " " + str(correct_ratio))
        ratio = ratio + correct_ratio
        
    print("test finished! avrg correct ratio is : "+str(ratio/999.0))
