import cv2
import numpy as np
import glob
import xgboost as xgb
from skimage.feature import local_binary_pattern
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class LBP():
    def __init__(self,P=8,R=1):
        self.point = P
        self.radius = R
        
class LBP_XG_Model():
    def __init__(self,P,R):
        self.lbp = LBP(P,R)
    def extract_LBP_feature(self,image):
        lbp = local_binary_pattern(image,self.lbp.P,self.lbp.R,'uniform')
        lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(257), density=True)  
        return lbp_hist
# class Hog():
  
def extract_hog_features(images):
    feature_list = []
    for img in images:
        features = hog(img, orientations=9, pixels_per_cell=(8, 8),
                       cells_per_block=(2, 2), block_norm='L2-Hys')
        feature_list.append(features)
    return np.array(feature_list)

# def train_xg_boost(train_df)