import cv2
import numpy as np

def watermarking(original, watermark, alpha = 0.5, width=500, height=500):
  # resize image
  original = cv2.resize(original, (width, height), interpolation = cv2.INTER_AREA)
  (originalHeight, originalWidth) = original.shape[:2]
  original = np.dstack([original, np.ones((originalHeight,originalWidth), dtype="uint8") * 255])

  #Resizing the image
  scale = 10
#   print(watermark.shape())
  rw = int(watermark.shape[1] * scale / 100)
  rh = int(watermark.shape[0] * scale / 100)
  dim = (rw,rh)
  watermarked = cv2.resize(watermark, dim, interpolation = cv2.INTER_AREA)
  (wH, wW) = watermarked.shape[:2]

  #Blending
  overlay = np.zeros((originalHeight, originalWidth, 3), dtype="uint8")
  overlay[10:10 + wH, 10:10 + wW] = watermarked
  final = original.copy()
  return cv2.addWeighted(overlay,0.5,final,1.0,0,final)


image = cv2.imread("E:\BQS\Code\sample_3.jpg")
watermark = cv2.imread("e:\BQS\Code\sample_1.jpg", cv2.IMREAD_UNCHANGED)
# Showing the result
final = watermarking(image, watermark)
cv2.imshow("Watermarked image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()
