# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 01:05:48 2020

@author: yss
"""

import matplotlib.pyplot as plt #导入Matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

x  =['武当派','峨眉派','华山派','嵩山派','少林派'] #此处也可数字
y1 =[0.340,0.587,0.291,0.232,0.214]
y2 =[0.414,0.398,0.156,0.180,0.211]
y3 =[0.335,0.026,0.173,0.220,0.301]
y4 =[0.085,0.030,0.018,0.217,0.289]

plt.figure(figsize = (16, 8)) #设置图像大小，当然可以设成方形（12,8）挺合适
plt.plot(x, y1, 'r-',label = '咽白菜变异系数',  linewidth = 2.5) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, 'g--', label = '喝芬达变异系数', linewidth = 2.5)
plt.plot(x, y3, 'b-.', label = '吃西瓜变异系数', linewidth = 2.5)
plt.plot(x, y4, 'k:', label = '啃馒头变异系数', linewidth = 2.5)

plt.plot(x, y1, 'or',markersize = 8) #作图，设置标签、线条颜色、线条大小
plt.plot(x, y2, '*g',markersize = 8)
plt.plot(x, y3, 'Db',markersize = 8)
plt.plot(x, y4, '^k',markersize = 8)

ax = plt.subplot(111) #这是画布哦，说明只在一张图显示，也可分割多图
plt.xticks(fontsize=20)#嗯调调字体
plt.yticks(fontsize=20)

plt.xlabel('武林派系 ', fontsize=25) # x轴名称
plt.ylabel('变异系数', fontsize=25) # y轴名称
# plt.title('A Simple Example') #标题
plt.ylim(0, 0.7) #显示的y轴范围
plt.legend(fontsize=20) #显示图例
plt.show() #显示作图结果

