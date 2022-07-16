# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：novelty_detection.py ， 异常检测部分
@Author  ：leeqingshui
@Date    ：2022/7/7 3:13 
'''

import pickle
import numpy as np
from math import ceil
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# 数据预处理
def pre_scaler(dataset, type_str="std"):
    if type_str == "minmax":
        scaler = MinMaxScaler()
    elif type_str == "std":
        scaler = StandardScaler()
    else:
        return None
    scaler.fit(dataset)
    return scaler, scaler.transform(dataset)

# 数据集拆分
def train_test_split(dataset, test_ratio=0.3, seed=42):
    if seed:
        np.random.seed(seed)
    shuffle_index = np.random.permutation(len(dataset))
    test_size = ceil(len(dataset) * test_ratio)
    test_index = shuffle_index[:test_size]
    train_index = shuffle_index[test_size:]
    dataset_train = dataset[train_index]
    dataset_test = dataset[test_index]
    return dataset_train, dataset_test

# 模型训练
def train_model():


if __name__ == '__main__':
