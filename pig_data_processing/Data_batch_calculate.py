# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：Data_batch_calculate.py , 批量处理生猪运动数据
@Author  ：leeqingshui
@Date    ：2022/7/5 20:36 
'''
import numpy as np
from matplotlib import pyplot as plt
import random

from Data_save import dataset_save
from feature_correlation_calculation import correlation_calculation
from Data_PCA import Data_PCA_Operation

#  ===========================================功能函数======================================================
'''
@ 函数功能                                   ：绘出多只生猪运动数据柱状图
@ 入口参数 {list}   average_motioninfo_list  ：生猪运动数据一维列表
@ 入口参数 {str}    img_save_path            ：标注后图片的保存路径
@ 入口参数 {str}    info_type                ：运动信息种类，包括：
@                                             距离       ：'distance'
@                                             加速度     ：'accelerated_speed'
@                                             平均速度   ：'average_speed'
@                                             最大速度   ：'max_speed'
@                                             最大加速度 ：'max_acc'
'''
def Show_Motion_Conv(average_motioninfo_list,img_save_path,info_type):

    # 横轴数据，生猪序号
    x_data = range(1,len(average_motioninfo_list)+1)
    y_data = average_motioninfo_list

    # 画图，plt.bar()可以画柱状图
    for i in range(len(y_data)):
        plt.bar(x_data[i], y_data[i])

    # 设置图片名称
    plt.title("Histogram of "+info_type+" comparison of multiple target pigs")
    # 设置x轴标签名
    plt.xlabel("pig id")
    # 设置y轴标签名
    plt.ylabel(info_type)
    # 保存图片
    plt.savefig(img_save_path+'\\'+"Histogram_of_"+info_type+"_comparison_of_multiple_target_pigs" +'.jpg', dpi=300)
    # 显示
    plt.show()


'''
@ 函数功能                            ：生成运动数据
@ 入口参数 {list}   mu                ：均值
@ 入口参数 {str}    sigma             ：方差
@ 入口参数 {str}    num               ：数量
@ 返回参数 {list}   move_info_list    ：生猪运动数据列表
'''
def Generate_Move_Data(mu, temp_mu, temp_sigma, sigma = 1, num = 100):

    move_info_list = abs(np.random.normal(mu, sigma, num))
    move_info_list = move_info_list.tolist()

    temp_list = abs(np.random.normal(temp_mu, temp_sigma, 92))
    temp_list = temp_list.tolist()

    move_info_list = move_info_list + temp_list

    return move_info_list

'''
@ 函数功能                                 ：生成三维散点图
@ 入口参数 {list}   average_distance_list  ：生猪运动距离数据列表
@ 入口参数 {list}   average_speed_list     ：生猪运动速度数据列表
@ 入口参数 {list}   average_acc_list       ：生猪运动加速度数据列表
'''
def Show_3D_Scatter(average_distance_list,average_speed_list,average_acc_list,save_path = "F:\\pig_healthy\\code\\pig_data_processing\\multi_result\\multi_pig_move_result_conv"):

    x = average_distance_list
    y = average_speed_list
    z = average_acc_list

    ax = plt.subplot(projection='3d')  # 创建一个三维的绘图工程
    ax.set_title('Show 3D Scatter of Pig Move info')  # 设置本图名称
    ax.scatter(x, y, z, c='r')  # 绘制数据点 c: 'r'红色，'y'黄色，等颜色

    ax.set_xlabel('pig_average_distance')  # 设置x坐标轴
    ax.set_ylabel('pig_average_speed')     # 设置y坐标轴
    ax.set_zlabel('pig_average_acc')        # 设置z坐标轴

    plt.savefig(save_path+'\\'+'3D_Scatter_of_Pig_Move_info'+'.jpg', dpi=300)
    plt.show()

'''
@ 函数功能                                 ：生成三维散点图
@ 入口参数 {list}   Operation_list         : 降维后矩阵数据
@ 入口参数 {str}    save_path              : 保存位置
'''
def Show_2D_Scatter(Operation_list, save_path):
    # 两个特征列表
    x_list = []
    y_list = []

    for data in Operation_list:
        x_list.append(data[0])
        y_list.append(data[1])

    # 创建一个二维的绘图工程
    ax = plt.subplot(111)
    # 设置本图名称
    ax.set_title('Show 2D Scatter of Pig Move info')
    # 设置x坐标轴
    ax.set_xlabel('pig move feture 1')
    # 设置y坐标轴
    ax.set_ylabel('pig move feture 2')
    plt.plot(x_list, y_list, 'ro')

    plt.savefig(save_path, dpi=300)
    plt.show()

#  ===========================================全局变量======================================================

# 图片保存地址
save_path = "F:\\pig_healthy\\code\\pig_data_processing\\multi_result\\multi_pig_move_result_conv"
# csv文件保存地址
csv_save_path = 'F:\\pig_healthy\\code\\pig_data_processing\\multi_result'+'\\'+'dataset.csv'
# 相关系数矩阵热力图保存地址
correlation_heatmap_save_path = 'F:\\pig_healthy\\code\\pig_data_processing\\multi_result'+'\\'+'correlation_heatmap.jpg'
# 降维度后二维散点图保存地址
Data_2D_Scatter_img_save_path = 'F:\\pig_healthy\\code\\pig_data_processing\\multi_result'+'\\'+'Data_2D_Scatter.jpg'

#  ===========================================主要流程======================================================

#  ++++++++++++++++++++++++++生成运动距离数据++++++++++++++++++++++++++++++++++

# 运动距离参数
average_distance_mu         = 4.86
average_distance_sigma      = 0.5
average_distance_list_num   = 100
average_distance_temp_mu    = 1
average_distance_temp_sigma = 0.9

# 生成数据
average_distance_list = Generate_Move_Data(
                                            mu         = average_distance_mu,
                                            sigma      = average_distance_sigma,
                                            num        = average_distance_list_num,
                                            temp_mu    = average_distance_temp_mu,
                                            temp_sigma = average_distance_temp_sigma
                                          )
# 打乱数据
random.shuffle(average_distance_list)

Show_Motion_Conv(average_motioninfo_list = average_distance_list,
                 img_save_path           = save_path,
                 info_type               = 'distance',
                 )

#  ++++++++++++++++++++++++++生成运动平均速度数据++++++++++++++++++++++++++++++++++

# # 运动速度参数
# average_speed_mu            = 0.26
# average_speed_sigma         = 0.1
# average_speed_list_num      = 100
# average_speed_temp_mu       = 0.1
# average_speed_temp_sigma    = 0.3
#
# # 生成数据
# average_speed_list = Generate_Move_Data(
#                                             mu         = average_speed_mu,
#                                             sigma      = average_speed_sigma,
#                                             num        = average_speed_list_num,
#                                             temp_mu    = average_speed_temp_mu,
#                                             temp_sigma = average_speed_temp_sigma
#                                         )
# # 打乱数据
# random.shuffle(average_speed_list)

average_speed_list = []

for distance in average_distance_list:
    speed = distance/(200+random.randint(0,200))
    average_speed_list.append(speed)

Show_Motion_Conv(average_motioninfo_list = average_speed_list,
                 img_save_path           = save_path,
                 info_type               = 'average_speed'
                 )

#  ++++++++++++++++++++++++++生成运动加速度数据++++++++++++++++++++++++++++++++++

# 运动加速度参数
average_acc_mu            = 0.25
average_acc_sigma         = 0.5
average_acc_list_num      = 100
average_acc_temp_mu       = 0.12
average_acc_temp_sigma    = 0.5

# 生成数据
average_acc_list = Generate_Move_Data(
                                            mu         = average_acc_mu,
                                            sigma      = average_acc_sigma,
                                            num        = average_acc_list_num,
                                            temp_mu    = average_acc_temp_mu,
                                            temp_sigma = average_acc_temp_sigma
                                        )
# 打乱数据
random.shuffle(average_acc_list)

Show_Motion_Conv(average_motioninfo_list = average_acc_list,
                 img_save_path           = save_path,
                 info_type               = 'average_acc'
                 )

#  ===========================================数据展示======================================================
# 展示3D散点图
Show_3D_Scatter(average_distance_list,average_speed_list,average_acc_list,save_path)

#  ===========================================数据保存======================================================
# 每一行代表一个样本
# 每一行的第一列表示生猪运动距离、第二列表示运动平均速度、第三列表示运动加速度的平均值
dataset_save(
            average_distance_list = average_distance_list,
            average_speed_list    = average_speed_list,
            average_acc_list      = average_acc_list,
            save_path             = csv_save_path
            )

#  ===========================================特征分析======================================================
# 计算三个特征的相关系数，并将相关系数矩阵热力图保存
correlation_calculation(
                        csv_path  = csv_save_path,
                        save_path = correlation_heatmap_save_path
                        )

#  ===========================================特征降维======================================================
# PCA特征降维度
Operation_list = Data_PCA_Operation(
                    average_distance_list = average_distance_list,
                    average_speed_list    = average_speed_list,
                    average_acc_list      = average_acc_list
                  )

print(Operation_list)

# 将降维度后数据以二维散点图形式显示
Show_2D_Scatter(
                Operation_list = Operation_list,
                save_path      = Data_2D_Scatter_img_save_path
               )





