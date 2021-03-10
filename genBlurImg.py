import cv2
import matplotlib.pyplot as plt
import numpy as np


def motion_blur(orig_image, kernel_image):
    kernel_image = kernel_image.astype(np.float32)
    kernel_image /= np.sum(kernel_image)
    return cv2.filter2D(orig_image, -1, kernel_image, borderType=cv2.BORDER_REPLICATE)

for name in range (133484,200001):
    image_id = '{0:07d}'.format(name)
    print(image_id)
    orig_image_path = "./data2/%s_orig.png" % image_id
    kernel_image_path = "./data2/%s_psf.png" % image_id
    orig_image = cv2.imread(orig_image_path, -1)
    kernel_image = cv2.imread(kernel_image_path, -1)
    add_blur = motion_blur(orig_image, kernel_image)
    cv2.imwrite('./data2/'+image_id + '_blur.png',add_blur )
