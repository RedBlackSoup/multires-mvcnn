## Multires-MVCNN

本项目根据《Volumetric and Multi-View CNNs for Object Classification on 3D Data》中提及的多分辨率MVCNN实现，其中目录结构如下：

ModelNet_OFF2MAT：将OFF的网格模型转换为三维张量，保存为MAT文件。

ModelNet_Mat2PNG：根据MAT渲染多世界的PNG图片。

mvcnn：根据https://github.com/jongchyisu/mvcnn_pytorch 修改，作为基线模型。

multires-mvcnn：我们根据论文对mvcnn进行多分辨率改进，并且实现自己的改进。

数据集来自ModelNet40（PRINCETON MODELNET）

https://modelnet.cs.princeton.edu/

我们的数据地址

https://drive.google.com/drive/folders/1ybgt-QEx0rMeyR1XJ_1GSqTp-bR1cqCR?usp=sharing

