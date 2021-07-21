## 简介

ModelNet_Mat2PNG实现了对mat文件的球体渲染与标准渲染，此处的mat文件是由OFF2MAT生成的30x30x30、60x60x60或者300x300x300的三维张量；渲染的图片将根据不同的方位角和仰角对模型进行拍摄，以达到数据增强的目的。

## 修改路径参数

按照自己电脑上对应的文件目录，修改3D模型数据和生成的图像的文件夹路径

```python
# mat文件夹路径
ModelNet_filepath = '对应体素数据的文件夹目录'
# png文件夹路径
ModelNet_voxel_20 = '对应生成的图像的文件夹目录'
```

以我的电脑为例，想要生成对应 30 * 30 * 30 体素数据的图像，文件夹路径应设置如下：

```python
# mat文件夹路径
ModelNet_filepath = 'ModelNet_voxelized_mat_30'
# png文件夹路径
ModelNet_voxel_20 = 'ModelNet_voxel_20views_30'
```

## 选择哪些类别的数据来生成图像

数据集中共有以下10种类别，您可以通过改变inclass数据元素来选择其中的一个或几个类别进行渲染并生成图像。

```python
inclass = ['bed', 'bench', 'chair', 'cup', 'dresser', 'flower_pot', 'stool', 'sofa', 'table', 'xbox']
```

## 运行代码

进入项目文件夹目录（ModelNet_Mat2PNG）后，在命令行输入以下代码运行程序即可：

> python ModelNet_mat2png_30_60.py

当然也可以打开ModelNet_mat2png_30_60.py运行程序，同理，想要获取标准渲染的3D模型，可以使用以下命令：

> python ModelNet_mat2png_norm.py

同时，如果您对图片的生成过程存在疑问，可以运行：

> python ModelNet_mat2png_singleshow.py

来查看单个图片的展示。

## 参数说明

设置仰角，此处仰角分别为30与-30：

> ele_angle = [30, -30]

设置方位角：

> azi_angle = range(0, 360, 36)

调整图像尺寸

> mlab.figure(size=(224, 224))