import numpy as np
from mayavi import mlab
from scipy.io import loadmat

mat_filepath = './bed_30.mat'

# mat文件类似字典 通过变量名索引 可以获取mat中的高维矩阵
voxelmat= loadmat(mat_filepath)['instance']

# 场景初始化
mlab.clf() 
mlab.figure(bgcolor=(1, 1, 1))
# size=(227, 227)
# 获取当前句柄
figure = mlab.gcf()

# 相机设置
mlab.view(azimuth = 0, elevation = 90, distance = None, focalpoint = 'auto', roll=None, reset_roll=True, figure=None)

# 非0点的xyz坐标
x,y,z=np.nonzero(voxelmat)

# 绘制的点的个数
count = x.shape[0]
x, y, z = x*0.1, y*0.1, z*0.1

# 用mlab.points3d绘制sphere
mlab.points3d(x, y, z, color=(0.9, 0.9, 0.9), mode = 'sphere', resolution=12, scale_factor = 0.1732)

# 设置缩放系数
figure.scene.camera.zoom(1.25)

mlab.show()

