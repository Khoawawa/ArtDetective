import cv2
import numpy as np
import glob
import xgboost as xgb
from sklearn.datasets import load_digits
from skimage.feature import local_binary_pattern
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import Tuple
class LBP():
    def __init__(self,P=8,R=1):
        self.point = P
        self.radius = R
        
    def extract_LBP_feature(self,image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        lbp = local_binary_pattern(image,self.point,self.radius,'uniform')
        lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(257), density=True)  
        return lbp_hist  
    
class XG():
    def __init__(self):
        self.model: xgb.XGBClassifier  = xgb.XGBClassifier(verbosity = 1)
        
    def fit(self,X_train,y_train,eval_set:list[Tuple]):
        self.model.fit(X_train,y_train,eval_set=eval_set, verbose= True)
        
    def predict(self,X):
        return self.model.predict(X)
    
class LBP_XG_Model(LBP,XG):
    def __init__(self,P=8,R=1):
        LBP.__init__(self,P,R)
        XG.__init__(self)
        
    def fit(self,X_train,y_train):
        X_features = np.array([self.extract_LBP_feature(img_path) for img_path in X_train])
        super().fit(X_features,y_train)
    
    def predict(self,image_path):
        feature = self.extract_LBP_feature(image_path).reshape(1,-1)
        return super().predict(feature)
    
    def save_model(self, model_path="lbp_xgboost.model"):
        """ Save the trained XGBoost model """
        self.model.save_model(model_path)
        print(f"Model saved to {model_path}")

    def load_model(self, model_path="lbp_xgboost.model"):
        """ Load the trained XGBoost model """
        self.model.load_model(model_path)
        print(f"Model loaded from {model_path}")