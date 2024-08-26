import numpy as np
import cv2

# Load ảnh từ file
#biến cờ có 3 gtri: 
img = cv2.imread('E:\\BQS\\Code\\sample_1.jpg', 0)

# Chia ảnh thành các khối 8x8
blocks = np.zeros((img.shape[0]//8, img.shape[1]//8, 8, 8))
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[1]):
        blocks[i, j] = img[i*8:(i+1)*8, j*8:(j+1)*8]

# Thực hiện phép biến đổi DCT trên từng khối
dct_blocks = np.zeros_like(blocks)
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[1]):
        dct_blocks[i, j] = cv2.dct(blocks[i, j].astype(np.float32))

# Lưu trữ các hệ số DCT vào một ma trận
dct_matrix = np.zeros((blocks.shape[0]*blocks.shape[1], 8, 8))
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[1]):
        dct_matrix[i*blocks.shape[1]+j] = dct_blocks[i, j]

# Giải mã ảnh từ các hệ số DCT
decoded_blocks = np.zeros_like(dct_blocks)
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[1]):
        decoded_blocks[i, j] = cv2.idct(dct_blocks[i, j].astype(np.float32))

# Gộp các khối ảnh đã được giải mã thành ảnh gốc
decoded_img = np.zeros_like(img)
for i in range(decoded_blocks.shape[0]):
    for j in range(decoded_blocks.shape[1]):
        decoded_img[i*8:(i+1)*8, j*8:(j+1)*8] = decoded_blocks[i, j]

# Hiển thị ảnh gốc và ảnh được giải mã
cv2.imshow('Original Image', img)
cv2.imshow('Decoded Image', decoded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    