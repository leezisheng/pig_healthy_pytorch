# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：Data_show.py , 对数据进行展示，包括：
@                         1. 单个（多个）猪质心点运动轨迹在二值化和RGB背景图展示
@                         2. 单个或者多个生猪运动轨迹、运动速度、运动加速度热力图展示
@                         3. 多个生猪运动速度、运动距离、运动加速度、静止时间柱状图
@Author  ：leeqingshui
@Date    ：2022/6/21 2:02 
'''

import cv2 as cv
from matplotlib import pyplot as plt

# 读取背景mask文件路径
rgb_maskimg_path    = 'F:\\pig_healthy\\code\\pig_data_processing\\mask_rgb.jpg'
binary_maskimg_path = 'F:\\pig_healthy\\code\\pig_data_processing\\mask_binary.jpg'

'''
@ 函数功能                          ：单个猪质心点运动轨迹在二值化和RGB背景图展示，
@                                    同时将标注后图片保存到指定文件夹
@ 入口参数 {list}  center_move_list ：生猪质心运动列表，数据格式：
@                                    [[{frame},{x_center},{y_center}],...]
@ 入口参数 {str}   img_save_path    ：标注后图片的保存路径
'''
def Show_move_in_maskimg(center_move_list, img_save_path = '', pig_id = 0, color = (0, 0, 255)):

    print('================================显示背景RGB图像=======================================')
    # 读取图片
    rgb_mask_img = cv.imread(rgb_maskimg_path,1)
    # 显示图片
    cv.imshow('rgb mask img',rgb_mask_img)
    cv.waitKey(5)
    cv.destroyAllWindows()

    print('================================显示背景二值化图像=======================================')
    # 读取图片
    binary_mask_img = cv.imread(binary_maskimg_path,0)
    # 显示图片
    cv.imshow('binary mask img',binary_mask_img)
    cv.waitKey(5)
    cv.destroyAllWindows()

    for center_data in center_move_list:
        # center_data为 [{frame},{x_center},{y_center}]
        x_center = center_data[1]
        y_center = center_data[2]
        cv.circle(rgb_mask_img, (x_center, y_center), 5, color, -1)
        cv.circle(binary_mask_img, (x_center, y_center), 5, color, -1)

    # 显示图片
    cv.imshow(str(pig_id)+'_tag_in_rgbmaskimg',rgb_mask_img)
    cv.waitKey(5)
    cv.destroyAllWindows()

    # 显示图片
    cv.imshow(str(pig_id)+'_tag_in_binarymaskimg',binary_mask_img)
    cv.waitKey(5)
    cv.destroyAllWindows()

    cv.imwrite(img_save_path+'\\'+str(pig_id)+'_tag_in_rgbmaskimg.png', rgb_mask_img)
    cv.imwrite(img_save_path + '\\' +str(pig_id)+ '_tag_in_binarymaskimg.png', binary_mask_img)







