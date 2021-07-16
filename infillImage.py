import cv2
import numpy as np

# Open the image.
img = cv2.imread('image.png')

width = img.shape[1]
height = img.shape[0]
borderLength = max(width, height)

left_border = (borderLength - width) // 2
right_border = borderLength - width - left_border
top_border = (borderLength - height) // 2
bottom_border = borderLength - height - top_border

assert(left_border + right_border + width == borderLength)
assert(top_border + bottom_border + height == borderLength)

square_image = cv2.copyMakeBorder(
    img,
    left = left_border,
    right = right_border,
    top = top_border,
    bottom = bottom_border,
    borderType=cv2.BORDER_CONSTANT,
    value = [0,0,0] # black
)

# write the output.
cv2.imwrite('image-with-border.png', square_image)

# create mask
blank_canvas = np.zeros((height, width, 3))
#blank_canvas[:] = (255,255,255) # black
blank_canvas[:] = (0,0,0) # white

mask = cv2.copyMakeBorder(
    blank_canvas,
    left = left_border,
    right = right_border,
    top = top_border,
    bottom = bottom_border,
    borderType=cv2.BORDER_CONSTANT,
    #value = [0,0,0] # white
    value = [255,255,255] # black
)

cv2.imwrite('image-mask.png', mask)


# open images
input_image = cv2.imread('image-with-border.png')
mask_image = cv2.imread('image-mask.png', cv2.IMREAD_GRAYSCALE)

# in-fill the image
painted_image = cv2.inpaint(input_image, mask_image, 3, cv2.INPAINT_TELEA) # cv2.INPAINT_NS
cv2.imwrite('image-painted.png', painted_image)

# resize image
target_width = 512
target_height = 512
target_size = (target_width, target_height)
resized_image = cv2.resize(painted_image, dsize=target_size, interpolation=cv2.INTER_AREA)
cv2.imwrite('image-processed.png', resized_image)
