import torchvision.transforms as T
import cv2
from skimage import exposure

class Preprocessor:
    def __init__(self, img_size=(244,244),blur_kernel=(3,3)):
        self.img_size = img_size
        self.blur_kernel = blur_kernel
        
    def process(self, image_path):
        """Preprocess an image before LBP extraction."""
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Resize for consistency
        image = cv2.resize(image, self.img_size)
        
        # Apply Gaussian blur to reduce noise
        image = cv2.GaussianBlur(image, self.blur_kernel, 0)
        
        # Histogram Equalization (Enhances contrast)
        image = exposure.equalize_hist(image)

        return image