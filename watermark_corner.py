import cv2
import numpy as np

def watermarking(original, watermark, alpha=0.5, watermark_width_percent=10, corner=1):
    # Get dimensions of the original image
    original_height, original_width = original.shape[:2]

    # Calculate the width of the watermark based on the specified percentage of the original image's width
    watermark_width = int(original_width * watermark_width_percent / 100)

    # Resize the watermark image while preserving aspect ratio
    scale_factor = watermark_width / watermark.shape[1]
    watermark_height = int(watermark.shape[0] * scale_factor)
    watermark_resized = cv2.resize(watermark, (watermark_width, watermark_height))

    # Create an overlay with the same size as the original image
    overlay = np.zeros_like(original)

    # Calculate the position to place the watermark based on the specified corner
    if corner == 1:
        y_offset = 10
        x_offset = 10
    elif corner == 2:
        y_offset = 10
        x_offset = original_width - watermark_width - 10
    elif corner == 3:
        y_offset = original_height - watermark_height - 10
        x_offset = original_width - watermark_width - 10
    elif corner == 4:
        y_offset = original_height - watermark_height - 10
        x_offset = 10

    # Place the watermark on the overlay at the calculated position
    overlay[y_offset:y_offset + watermark_height, x_offset:x_offset + watermark_width] = watermark_resized

    # Blend the overlay with the original image
    final = cv2.addWeighted(overlay, alpha, original, 1.0, 0)

    return final

# Example usage:
original_image = cv2.imread('E:\BQS\Code\sample_3.jpg')
watermark_image = cv2.imread('E:\BQS\Code\sample_2.jpg', cv2.IMREAD_UNCHANGED)

# Interactive input for corner position
print("Choose a corner for placing the watermark:")
print("1. Top-left")
print("2. Top-right")
print("3. Bottom-right")
print("4. Bottom-left")
corner = int(input("Enter the number corresponding to the corner: "))

watermarked_image = watermarking(original_image, watermark_image, corner=corner)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
