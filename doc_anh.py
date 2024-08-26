import numpy as np
import cv2
import random

img = cv2.imread('E:\BQS\Code\sample_3.jpg', 1)

for i in  range (560):
    for j in range (972):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow("Hien thi", img)
#nếu không có waitkey thì cửa sổ hiện lên xong tắt
#nếu ko để gì thì nó đợi ấn phím bất kỳ là mất, còn lại set time theo mili giây
k = cv2.waitKey()

print(img.shape)