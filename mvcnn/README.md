## 简介

本代码来自于https://github.com/jongchyisu/mvcnn_pytorch

并对代码进行适度修改，适配了我们自己的dataset，该结果将作为网络性能的基准测试；同时也对网络添加了单类测试功能，以得到每个类的准确率。

## 代码运行

想要训练模型，可以使用以下代码：

> !python train_mvcnn.py -name model_result -num_models 300 -weight_decay 0.001 -num_views 20 -cnn_name alexnet

同时，如果想用已有模型进行测试，可以使用以下代码：

> !python test_mvcnn.py -name model_result-num_models 300 -num_views 20 -cnn_name alexnet

## 参数说明

-name: 模型名称

-bs: 批处理大小，默认为8，即每次处理8个3D模型（每个模型20张图片）

-num_models 每个类的最大模型数

-lr 学习率，默认为5e-5

-weight_decay 权值衰减，默认为0

-no_pretraining 是否使用预训练模型

-cnn_name 使用的cnn，可选有resnet18、resnet34、resnet50、alexnet、vgg11、vgg16

-num_views 每个模型包含的视图数，默认为20

-train_path 训练集路径

-val_path 测试集路径

