% addpath(genpath('polygon2voxel/'));

%============================================================
%  ReadMe
%  This code can be used to generate voxelized 3D mat files 
%  with different views from ModelNet10. 
%  The code is revised by me, but I forget the original author
%                        SO SORRY !!!
%         Any questions, Let Me Know, thanks....
%------------------------------------------------------------
%  Parameters:
%    volume_size: the output volume size is 300*300*300
%    angle_inc:   the multiview images are generated based
%                 on equal angle-interval sampling, the total
%                 num of images from one .OFF is 360/angle_inc
%    off_path:    the path of ModelNet10
%    mat_path:    the path of output voxelized mat files
%------------------------------------------------------------
%  Examples:
%  volume_size = 30;
%  angle_inc = 90;
%  OUTPUT: for each .OFF file, we can obtain 4(360/90) mat
%          files from different view angles, which are 0��90��
%          180��360��.
%============================================================

%----  Parameters needed to be changed  ------
volume_size = 30;
angle_inc = 90;

off_path='ModelNet10';
mat_path='ModelNet10_voxelized_mat';

% Classes of ModelNet10
modelnet10_classes = {'bathtub','bed','chair','desk','dresser','monitor','night_stand','sofa','table','toilet'};

% ModelNet_off2mat function
modelnet_off2mat(off_path,mat_path,modelnet10_classes,volume_size,angle_inc);

fprintf('******************* The END *****************')

