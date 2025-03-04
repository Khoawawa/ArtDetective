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
    def extract_LBP_feature(self,image):
        lbp = local_binary_pattern(image,self.point,self.radius,'uniform')
        lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(257), density=True)  
        return lbp_hist  
class XG():
    def __init__(self):
        self.model: xgb.XGBClassifier  = xgb.XGBClassifier()
    def fit(self,X_train,y_train):
        self.model.fit(X_train,y_train)
    def predict(self,X_target):
        return self.model.predict(X_target)
class LBP_XG_Model(LBP,XG):
    def __init__(self,P=8,R=1):
        LBP.__init__(self,P,R)

# def train_xg_boost(train_df)
if __name__ == "__main__":
    img = cv2.imread('test.jpg',0)
    print("Image type:", type(img))
    print("Image shape:", img.shape)
    lbp_hist = LBP_XG_Model().extract_LBP_feature(img)
    print(lbp_hist)
    import matplotlib.pyplot as plt
    plt.hist(lbp_hist,bins=256, color="gray", alpha=0.7)
    plt.show()