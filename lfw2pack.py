
import mxnet as mx
from mxnet import ndarray as nd
import argparse
import pickle
import sys
import os
import lfw
parser = argparse.ArgumentParser(description='Package LFW images')
# general
parser.add_argument('--data-dir', default='', help='')
# 修改１：图像大小修改为112，112
parser.add_argument('--image-size', type=str, default='112,112', help='')
parser.add_argument('--output', default='', help='path to save.')
# 修改2：添加解析参数　
parser.add_argument('--num-samepairs',default=100)
args = parser.parse_args()
lfw_dir = args.data_dir
image_size = [int(x) for x in args.image_size.split(',')]
# 修改3：将文件名pairs.txt修改成train.txt
lfw_pairs = lfw.read_pairs(os.path.join(lfw_dir, 'train.txt'))
print(lfw_pairs)
# 修改4：下一行进行修改成需要的格式
# lfw_paths, issame_list = lfw.get_paths(lfw_dir, lfw_pairs, 'jpg'）
lfw_paths, issame_list = lfw.get_paths(lfw_pairs,int(args.num_samepairs)+1)#, 'jpg')
lfw_bins = []
#lfw_data = nd.empty((len(lfw_paths), 3, image_size[0], image_size[1]))
print(len(issame_list))
i = 0
for path in lfw_paths:
  with open(path, 'rb') as fin:
    _bin = fin.read()
    lfw_bins.append(_bin)
    #img = mx.image.imdecode(_bin)
    #img = nd.transpose(img, axes=(2, 0, 1))
    #lfw_data[i][:] = img
    i+=1
    if i%1000==0:
      print('loading lfw', i)
with open(args.output, 'wb') as f:
  pickle.dump((lfw_bins, issame_list), f, protocol=pickle.HIGHEST_PROTOCOL)
