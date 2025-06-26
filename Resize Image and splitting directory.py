import os
import cv2
# Define the directory path
directory_path = r'F:\New folder (2)\Real' # Define the new size for resizing
new_size = (224, 224)
# Process each image in the directory
for filename in os.listdir(directory_path):
if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')): # Check for valid imagefileextensions
image_path = os.path.join(directory_path, filename)
try:
# Read the image
img = cv2.imread(image_path)
# Print the original shape of the image

print(f"Original image shape for {filename}:", img.shape)
# Resize the image
resized_img = cv2.resize(img, new_size)
# Print the resized shape of the image
print(f"Resized image shape for {filename}:", resized_img.shape)
# Save the resized image, overwriting the original file
cv2.imwrite(image_path, resized_img)
# Optionally display the resized image
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(1) # Display the image for a short moment
cv2.destroyAllWindows()
print(f'Processed and saved: {filename}')
except Exception as e:
print(f'Error processing {filename}: {e}')
print('All images have been processed and resized.')
