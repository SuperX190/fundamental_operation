import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 读取图像
img = cv.imread("D:\Python\Opencvlearn\pythonpath.png",1)   #0灰度图

# 2 显示图像
# 2.1 OPencv
# cv.imshow("pythonpath",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 2.2 matplotlib
# plt.imshow(img,cmap=plt.cm.gray)
# plt.show()

# 3 图像保存
cv.imwrite("D:\\Python\\Opencvlearn\\01.png",img) #汉字识别保存不了

