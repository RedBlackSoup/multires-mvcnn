'''
####Original path###
- ModelNet4_voxelized_mat_norm
	--bed
		--train/test
			--- bed_0001.mat
			--- bed_0002.mat
			.....
			--- bed_0224.mat
	--chair
		--train/test
			--- bed_0001.off

			
####Target path###
- ModelNet4_voxel_20views
	--bathtub
		--train/test
			--- bathtub_0001.off
				---- bathtub_0001_01.png
				---- bathtub_0001_02.png
							...
				---- bathtub_0001_20.png
			--- bathtub_0002.off
				---- bathtub_0002_01.png
				---- bathtub_0002_02.png
							...
				---- bathtub_0002_20.png
			.....
			--- bathtub_0300.off
				---- bathtub_0300_01.png
				---- bathtub_0300_02.png
							...
				---- bathtub_0300_20.png
	--bed
		--train/test
			--- bed_0001.off
				---- bed_0001_01.png
				---- bed_0001_02.png
							...
				---- bed_0001_20.png
#################################################'''

import numpy as np
import mayavi.mlab as mlab
from scipy.io import loadmat
import time, os

# mat文件夹路径
ModelNet_filepath = 'ModelNet_voxelized_mat_30'
# png文件夹路径
ModelNet_voxel_20 = 'ModelNet_voxel_20views_30'

# classpath for ModelNet10, change for your own dataset

# 设置数据类与镜头角度
inclass = ['bed', 'bench', 'chair', 'cup', 'dresser', 'flower_pot', 'stool', 'sofa', 'table', 'xbox']
ele_angle = [30, -30]
ele_angle = [i + 90 for i in ele_angle]
azi_angle = range(0, 360, 36)


# 调整图像尺寸
mlab.figure(size=(224, 224))
figure = mlab.gcf() 
figure.scene.camera.zoom(1.25)
# function: voxel mat 2 image(.png)
def voxel_mat2img(voxel_mat, png_savedir, voxelmat_path):
	if not os.path.exists(png_savedir):
		os.makedirs(png_savedir)
		print('voxel_image dir has been created')

	# 场景初始化
	mlab.clf() 

	# 绘制图像================================================================================

	# 非0点的xyz坐标
	x, y, z = np.nonzero(voxel_mat)

	# 绘制的点的个数
	count = x.shape[0]
	x, y, z = x * 0.1, y * 0.1, z * 0.1

	# 此处需要修改成球体渲染的代码
	# mlab.contour3d(voxel_mat, color = (0.9,0.9,0.9)) # 提供numpy标准数组
	mlab.points3d(x,y,z, color=(0.9, 0.9, 0.9), mode='sphere', resolution=12, scale_factor=0.1732)

	# =======================================================================================
	count = 0
	for ele in ele_angle:
		for azi in azi_angle:
			count += 1
			# 图片名称
			voxel_savename = voxelmat_path.split('.')[0]
			voxel_savename = os.path.split(voxel_savename)[-1]
			png_savepath = os.path.join(png_savedir, voxel_savename + "_" + str(count) + ".png")
			# if png is existed
			if os.path.exists(png_savepath):
				continue
			mlab.view(azimuth = azi, elevation = ele, distance = None, focalpoint = 'auto', roll=None, reset_roll=True, figure=None)
			# 设置图像大小

			# 保存图像
			mlab.savefig(png_savepath)
			print(png_savepath, 'saved##############')	
	return


# convert modelnet4_voxelized_mat to modelnet4_voxel_20views
def main():
	ModelNet_classpath = os.listdir(ModelNet_filepath)
	for classpath_index in ModelNet_classpath:
		if classpath_index not in inclass:
			continue

		voxelmat_class_ = os.path.join(ModelNet_filepath, classpath_index)
		# '.\ModelNet40_voxelized_mat\bed'
		class_split = os.listdir(voxelmat_class_)
		# class_split => train test

		for vc_split in class_split:
			voxelmat_class_split = os.path.join(voxelmat_class_, vc_split)
			# '.\ModelNet40_voxelized_mat\bed\train'
			voxelmat_class_list = os.listdir(voxelmat_class_split)
			# voxelmat_class_list => bed_0001.mat bed_0002.mat bed_0003.mat ....

			for voxelmat_list_index in voxelmat_class_list:
					voxelmat_list = os.path.join(voxelmat_class_split, voxelmat_list_index)
					# '.\ModelNet40_voxelized_mat\bed\train\bed_0001.mat'
					voxelmat_list_off = voxelmat_list_index.split('.')[0] + '.off'
					# 导入mat中的高维矩阵 voxelmat_是numpy张量
					voxelmat_ = loadmat(voxelmat_list)['instance']
					# 将voxelmat_转换为png图片(20张)
					voxel_img_savepath = os.path.join(ModelNet_voxel_20, classpath_index, vc_split, voxelmat_list_off)
					voxel_mat2img(voxelmat_, voxel_img_savepath, voxelmat_list)

if __name__ == '__main__':
	main()
	print("generation is finished! ##############")