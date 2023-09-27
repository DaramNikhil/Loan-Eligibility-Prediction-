import numpy as np

import pandas as pd

from sklearn.pipeline import  Pipeline

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import  StandardScaler,OneHotEncoder

from sklearn.compose import ColumnTransformer

from dataclasses import dataclass
import re
import os
import pickle
from utils import save_file

from data_training import Initialisation

@dataclass
class Data_Transform_config:
    
    feature_scale = os.path.join("data_files","processor.pkl")
  
   
class Data_Transformation:
    
    
    
    def __init__(self):
        
        self.Configure_files = Data_Transform_config()
        
    def Transform_pipeline(self):
        
        catagoricals = ["Gender",
        "Married","Education",
        
        "Property_Area"]
        
        numarics = ["Dependents",
        "CoapplicantIncome",
        "LoanAmount","Loan_Amount_Term","Credit_History"]
               
        numaric_pipeline = Pipeline(
        
                    steps=[
                    
                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scale",StandardScaler())
                    
                    ]
        
                )
                
        catagorical_pipeline = Pipeline(
        
               steps= [
            
                 ("imputer",SimpleImputer(strategy="most_frequent")),
                 ("ohe",OneHotEncoder()),
                 ("scale",StandardScaler(with_mean=False))
            
            ]
        
            )
            
        
        transform = ColumnTransformer(
        
                [
                
            
                ("numaricals",numaric_pipeline,numarics),
                ("catagoricals",catagorical_pipeline,catagoricals)
            
            ],remainder="drop"
        
        
            )
            
        return transform
                    
                
        
    def transforming_data(self,train_data,test_data):
        
        try:
            
            #preprocess the train_data
           train_data["Dependents"] = train_data["Dependents"].str.title()
            
           train_data["Dependents"] = train_data["Dependents"].replace("3+",3,regex=False)
           
           #preprocess the test data
           test_data["Dependents"] = test_data["Dependents"].str.title()
           
           test_data["Dependents"] = test_data["Dependents"].replace("3+",3,regex=False)
           
        
           feature_train_data = train_data.drop_duplicates()
           feature_test_data = test_data.drop_duplicates()
            
            
           train_data_frame = feature_train_data.drop(["Loan_Status","Loan_ID"],axis=1)
            
           train_target_frame = feature_train_data["Loan_Status"]
           
           mapping = {
           
               "Y":1,
               "N":0
           
           }
           
           #convert the catagorical values to numaric in target dtaa
           train_target_frame = feature_train_data["Loan_Status"].map(mapping)
            
           test_data_frame = feature_test_data.drop(["Loan_Status","Loan_ID"],axis=1)
            
           test_target_frame = feature_test_data["Loan_Status"].map(mapping)
           
           processor = self.Transform_pipeline()
            
           #train arry
           train_feature_arr = processor.fit_transform(train_data_frame)
           
           #test array
           test_feature_arr = processor.transform(test_data_frame)
           
           train_arr = np.c_[train_feature_arr,np.array(train_target_frame)]
           
           test_arr = np.c_[test_feature_arr,np.array(test_target_frame)]
           
           
           
           save_file(
           
               processor,self.Configure_files.feature_scale
           
           
           )
           
           return(
           
           train_arr,
           
           test_arr
           
           
           )
                                          
            
        except Exception as e:
            raise e
            
            