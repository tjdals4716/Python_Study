import cv2
import numpy as np

def compute_depth_map_ms1_1(left_img, right_img, num_scales=3):
    height, width = left_img.shape[:2]
    depth_map = np.zeros((height, width), dtype=np.float32)

    for scale in range(num_scales):
        scaled_left = cv2.resize(left_img, None, fx=1/(2**scale), fy=1/(2**scale), interpolation=cv2.INTER_LINEAR)
        scaled_right = cv2.resize(right_img, None, fx=1/(2**scale), fy=1/(2**scale), interpolation=cv2.INTER_LINEAR)
        
        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(scaled_left, scaled_right).astype(np.float32) / 16.0
        
        disparity_upscaled = cv2.resize(disparity, (width, height), interpolation=cv2.INTER_LINEAR)
        depth_map += disparity_upscaled / num_scales
    
    return depth_map

def compute_depth_map_ms1_2(left_img, right_img, num_scales=3):
    height, width = left_img.shape[:2]
    depth_map = np.zeros((height, width), dtype=np.float32)
    weight_sum = np.zeros((height, width), dtype=np.float32)

    for scale in range(num_scales):
        scaled_left = cv2.resize(left_img, None, fx=1/(2**scale), fy=1/(2**scale), interpolation=cv2.INTER_LINEAR)
        scaled_right = cv2.resize(right_img, None, fx=1/(2**scale), fy=1/(2**scale), interpolation=cv2.INTER_LINEAR)
        
        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(scaled_left, scaled_right).astype(np.float32) / 16.0
        
        disparity_upscaled = cv2.resize(disparity, (width, height), interpolation=cv2.INTER_LINEAR)
        
        weight = 1 / (2 ** scale)
        depth_map += weight * disparity_upscaled
        weight_sum += weight
    
    depth_map /= weight_sum
    return depth_map

# Example usage
left_image_path = 'MSD1-1.png'
right_image_path = 'MSD1-2.png'

left_img = cv2.imread(left_image_path, cv2.IMREAD_GRAYSCALE)
right_img = cv2.imread(right_image_path, cv2.IMREAD_GRAYSCALE)

depth_map_ms1_1 = compute_depth_map_ms1_1(left_img, right_img)
depth_map_ms1_2 = compute_depth_map_ms1_2(left_img, right_img)

# Normalize depth maps for visualization
depth_map_ms1_1 = cv2.normalize(depth_map_ms1_1, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
depth_map_ms1_2 = cv2.normalize(depth_map_ms1_2, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Save the depth maps
cv2.imwrite('depth_map_ms1_1.png', depth_map_ms1_1)
cv2.imwrite('depth_map_ms1_2.png', depth_map_ms1_2)

# Display the depth maps
cv2.imshow('Depth Map MSDM1-1', depth_map_ms1_1)
cv2.imshow('Depth Map MSDM1-2', depth_map_ms1_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
