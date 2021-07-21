# README

这个代码用于将off文件转化为mat文件 具体为 ModelNet10 或 40 数据集的off文件 

---

* 参数:

volume_size: 输出的体素的大小为 volume_size×volume_size×volume_size

angle_inc:   每次绕z轴旋转的角度

off_path:    off文件的路径

mat_path:    mat文件的路径

phi:         仰角和俯角

* 使用：

对于ModelNet10数据，可以直接运行 ModelNet10_off2mat.m 文件

对于ModelNet40数据，可以直接运行 ModelNet40_off2mat.m 文件

* 旋转控制：

R1: 水平旋转矩阵 ，水平旋转

R2: 仰角旋转矩阵 ，改变仰角

* 样例：

运行ModelNet10_off2mat.m文件，获得ModelNet10文件中bathtub模型的train数据集的off文件对应的旋转后的mat矩阵