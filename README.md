## 运行环境

```
torch                  1.6.0
torchvision            0.7.0
python                 3.7.2
Pillow                 7.1.2
opencv-python          4.2.0.32
```

## 使用

作者使用英文数据集训练用于英文文本去模糊，数据集下载链接参考data文件夹下的链接。

我们使用的是自己制作的中文数据集，用于中文文本去模糊，textToImg.py文件是读取一个文本，将其转化成图片形式，图片格式满足训练集要求，然后将源数据集的psf.png文件复制到自制数据集上。然后使用genBlurImg.py来模糊图片，即可完成自制数据集。也可以使用作者的方法，从现实的文本中制作数据集。由于中文笔画太多并且汉字太多，中文文本去模糊可能效果不是很好，我们扩充了数据集，genfilelist.py用于扩充训练集的文件列表。以上代码的使用可以根据需求更改，代码鲁棒性不够好。

### 训练

运行python train.py开始训练，后面可以跟一些参数，--batch_size指定批次大小，--train_data指定包含训练数据集目录的txt文件，--eval_data指定评估的数据，--exp_dir指定输出的评估文件目录以及模型保存的目录，--backbone指定骨干网络，"--num_workers指定线程数，--max_epoches指定训练轮数，--optim指定优化的网络，默认可直接运行python train.py即可开始训练。

### 测试

运行python load_and_test.py，--blurimg参数指定模糊图片路径，--train_model指定训练模型保存的路径，--backbone指定训练时用的骨干网，即可测试模糊的图像的去模糊效果，测试结果输出在test目录下。

