import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn
import os,shutil,json
import argparse

from tools.Tester import ModelNetTester
from tools.ImgDataset import MultiviewImgDataset, SingleImgDataset
from models.MVCNN import MVCNN, SVCNN

parser = argparse.ArgumentParser()
parser.add_argument("-name", "--name", type=str, help="Name of the experiment", default="MVCNN")
parser.add_argument("-bs", "--batchSize", type=int, help="Batch size for the second stage", default=8)# it will be *12 images in each batch for mvcnn
parser.add_argument("-num_models", type=int, help="number of models per class", default=200)
parser.add_argument("-no_pretraining", dest='no_pretraining', action='store_true')
parser.add_argument("-cnn_name", "--cnn_name", type=str, help="cnn model name", default="vgg11")
parser.add_argument("-num_views", type=int, help="number of views", default=20)
parser.add_argument("-val_path", type=str, default="../data/ModelNet4_voxel_20views_30/*/test/*")
parser.set_defaults(train=False)


if __name__ == '__main__':
    args = parser.parse_args()
    pretraining = not args.no_pretraining

    # no pretraining: false
    # train: false
    # STAGE 1

    cnet = SVCNN(args.name, nclasses=10, pretraining=pretraining, cnn_name=args.cnn_name)
    cnet.load(args.name+'_stage_1')
    
    # # 定义测试集
    # val_dataset = SingleImgDataset(args.val_path, scale_aug=False, rot_aug=False, test_mode=True)
    # val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=0)
    
    # # 数据集中的文件数
    # print('num_val_files: '+str(len(val_dataset.filepaths)))

    # tester = ModelNetTester(cnet, val_loader, nn.CrossEntropyLoss(), 'svcnn', num_views=1)
    # tester.validation_accuracy()

    # STAGE 2

    cnet_2 = MVCNN(args.name, cnet, nclasses=10, cnn_name=args.cnn_name, num_views=args.num_views)
    del cnet
    cnet_2.load(args.name+'_stage_2')

    
    val_dataset = MultiviewImgDataset(args.val_path, scale_aug=False, rot_aug=False, num_views=args.num_views)
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=args.batchSize, shuffle=False, num_workers=0)
    
    # 数据集中的文件数
    print('num_val_files: '+str(len(val_dataset.filepaths)))

    tester = ModelNetTester(cnet_2, val_loader, nn.CrossEntropyLoss(), 'mvcnn', num_views=args.num_views)
    tester.validation_accuracy()


