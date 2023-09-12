#bend upward
import cv2
import numpy as np
import random

def bend_image(image, bend_factor):
    height, width, _ = image.shape
    bent_img = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            new_x = x
            new_y = int(y - bend_factor * x * (width - x) / width)
            if 0 <= new_x < width and 0 <= new_y < height:
                bent_img[new_y, new_x] = image[y, x]

    return bent_img

# Create a white blank image
height, width = 1000, 1000
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Apply bending effect (upward)
bu = random.uniform(0, 2)
bend_factor = bu # Adjust this value for desired bending
bent_img = bend_image(image, bend_factor)

# Display and save the bent image
cv2.imshow('Bent Image', bent_img)
cv2.imwrite('bent_image_upward.png', bent_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
