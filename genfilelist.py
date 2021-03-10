import random

train = open("./data_train.txt",'w')
test = open("./data_test.txt",'w')
data_all = open("./all.txt",'w')


for name in range (0,200001):
    image_id = '{0:07d}'.format(name)
    orig_image_path = "data/%s_orig.png " % image_id
    blur_image_path = "data/%s_blur.png " % image_id
    kernel_image_path = "data/%s_psf.png\n" % image_id
    try:
        data_all.write(orig_image_path + blur_image_path + kernel_image_path)
        if(random.random() > 0.78):
            test.write(orig_image_path + blur_image_path + kernel_image_path)
        else:
            train.write(orig_image_path + blur_image_path + kernel_image_path)
    except Exception as e: 
            print(e)
train.close()
test.close()
data_all.close()
print("生产完成！")
