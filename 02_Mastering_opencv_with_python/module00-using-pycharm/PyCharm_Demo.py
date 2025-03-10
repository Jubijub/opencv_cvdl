import cv2
import matplotlib.pyplot as plt

# Read image as grayscale.
bw_img = cv2.imread('img_bw_18x18.png', cv2.IMREAD_GRAYSCALE)

# Print the image data (pixel values) of a 2D NumPy array.
# Each pixel value is 8-bits in the range [0, 255].
print(bw_img)

# Print the size of image.
print('Image size is ', bw_img.shape)

# Print data-type of image.
print('Data type of image is ', bw_img.dtype)

# Set color map to gray scale for proper rendering.
plt.figure(figsize=[5, 5])
plt.imshow(bw_img, cmap='gray')
plt.show()  # <-- Add this line to display the image.

# Read image as gray scale.
MNIST_3_img = cv2.imread('MNIST_3_18x18.png', cv2.IMREAD_GRAYSCALE)
print(MNIST_3_img)

# Display the image.
plt.figure(figsize=[5, 5])
plt.imshow(MNIST_3_img, cmap='gray')
plt.show()  # <-- Add this line to display the image.

# Load a color image.
image = cv2.imread('Apollo-8-Launch.jpg')
plt.figure(figsize=[5, 5])
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert to RGB for correct color display.
plt.title('Apollo-8-Launch.png', fontsize=16)
plt.show()  # <-- Add this line to display the image.

# Function to draw text on an image.
def drawBannerText(frame, text, banner_height_percent=0.05, text_color=(0, 255, 0)):
    # Draw a black filled banner across the top of the image frame.
    banner_height = int(banner_height_percent * frame.shape[0])
    cv2.rectangle(frame, (0, 0), (frame.shape[1], banner_height), (0, 0, 0), thickness=-1)

    # Draw text on the banner.
    left_offset = 20
    location = (left_offset, int(5 + (banner_height_percent * frame.shape[0]) / 2))
    fontScale = 1.2
    fontThickness = 2
    cv2.putText(frame, text, location, cv2.FONT_HERSHEY_PLAIN, fontScale, text_color, fontThickness, cv2.LINE_AA)

# Apply the function to draw text on the image.
drawBannerText(image, "Apollo 8 Saturn V Launch, 1968", banner_height_percent=0.05, text_color=(0, 255, 0))

# Display the updated image with the text.
plt.figure(figsize=[5, 5])
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert to RGB for correct color display.
plt.show()  # <-- Add this line to display the image.