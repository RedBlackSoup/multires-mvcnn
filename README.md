## Multires-MVCNN

本项目根据《Volumetric and Multi-View CNNs for Object Classification on 3D Data》中提及的多分辨率MVCNN实现，其中目录结构如下：

ModelNet_OFF2MAT：将OFF的网格模型转换为三维张量，保存为MAT文件。

ModelNet_Mat2PNG：根据MAT渲染多世界的PNG图片。

mvcnn：根据https://github.com/jongchyisu/mvcnn_pytorch修改，作为基线模型。



数据集来自ModelNet40（PRINCETON MODELNET）

https://modelnet.cs.princeton.edu/