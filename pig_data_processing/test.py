# -*- coding: UTF-8 -*-
'''
@Project ：code ，对Data_calculate.py、Data_parsing.py、Data_show.py中函数进行测试
@File    ：test.py
@Author  ：leeqingshui
@Date    ：2022/6/21 2:44 
'''

from Data_parsing import openreadtxt,Data_format_trans,Get_move_data
from Data_calculate import Get_CenterMoveData_List, Get_MoveDistance_List, Get_total_distance
from Data_show import Show_move_in_maskimg

# 测试txt文件路径
test_txt_path = "F:\\pig_healthy\\code\\output\\results.txt"
# 选定要看的目标生猪序号
pig_id = 8
# 结果图片保存地址
result_img_save_path = 'F:\\pig_healthy\\code\\pig_data_processing\\result\\center_move_in_mask'

# ============================从txt文件中解析数据=======================================
print('==============================================================================')
print('开始解析文件：'+test_txt_path+'中数据')

try:
    # 读取txt文件中每一行数据，保存到line_data_list中
    line_data_list = openreadtxt(test_txt_path)
    # 对行数据二维列表中元素从字符串格式到int格式进行转换
    line_data_list = Data_format_trans(line_data_list)
    # 选出id号代表的某头猪的运动轨迹数据列表
    move_data_list = Get_move_data(line_data_list , pig_id)
    print('解析文件中数据成功')
except:
    print('解析文件中数据失败')

# 输出固定序号生猪的质心运动列表
# 数据格式：[[{frame},{x_center},{y_center}],...]
center_move_list = Get_CenterMoveData_List(move_data_list)

# 显示并保存标注轨迹点后背景图片
Show_move_in_maskimg(center_move_list, img_save_path = result_img_save_path, pig_id = pig_id, color = (0, 0, 255))
# print(center_move_list)

# 计算移动距离，获得每一帧下移动距离的列表
move_distance_list = Get_MoveDistance_List(center_move_list)
# print(move_distance_list)

# 计算总运动距离
total_distance = Get_total_distance(move_distance_list)
print('序号为：'+str(pig_id)+'的生猪总移动距离为：'+str(total_distance)+'(m)')