import cv2
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.datasets import load_digits
from skimage.feature import local_binary_pattern
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import Tuple
from Processor import Preprocessor



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
    def score(self,X,y):
        return self.model.score(X,y)
    
class LBP_XG_Model():
    def __init__(self,transform: Preprocessor,P=8,R=1):
        self.lbp = LBP(P,R)
        self.xg = XG()
        self.transform = transform
        
    def fit(self,X_train,y_train,eval_set=None):
        if eval_set is None:
            eval_set = [(X_train,y_train)]
        X_features = np.array([self.lbp.extract_LBP_feature(img_path) for img_path in X_train])
        self.xg.fit(X_features,y_train)
    
    def predict(self,X: pd.Series) -> list:
        X_transform = [self.transform.process(img_path) for img_path in X]
        features = [self.lbp.extract_LBP_feature(image_path).reshape(1,-1) for image_path in X_transform]
        return [self.xg.predict(feature) for feature in features]   
    
    def score(self,X,y):
        return self.xg.score(X,y)
    
    def save_model(self, model_path="lbp_xgboost.model"):
        """ Save the trained XGBoost model """
        self.xg.model.save_model(model_path)
        print(f"Model saved to {model_path}")

    def load_model(self, model_path="lbp_xgboost.model"):
        """ Load the trained XGBoost model """
        self.xg.model.load_model(model_path)
        print(f"Model loaded from {model_path}")