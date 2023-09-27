import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
from data_transform import Data_Transformation
from data_training import Initialisation

from prediction_pipeline import prediction

class Data_Ingestion_Configuration:
    
    raw_data = os.path.join("data_files","data.csv")
    train_data = os.path.join("data_files","train_data.csv")
    test_data  = os.path.join("data_files","test_data.csv")
      
    
class Data_Ingestion:
    
    def __init__(self):
        self.data = Data_Ingestion_Configuration()
        
    def Data_ingestion_implimentation(self):
        
        try:
            
            data_file = pd.read_csv("/storage/emulated/0/loan_eligibility_prediction/data/Loan_Data.csv")
                        
            
           #create a files to store the train& test samples
           
            os.makedirs(os.path.dirname(self.data.raw_data),exist_ok=True)
            os.makedirs(os.path.dirname(self.data.train_data),exist_ok=True)
            os.makedirs(os.path.dirname(self.data.test_data),exist_ok=True)
            
            data_file.to_csv(self.data.raw_data,header=True,index=False)
            
            train_data, test_data = train_test_split(data_file,test_size=0.2,random_state=41)
            
            train_data.to_csv(self.data.train_data,header=True,index=False)
            
            test_data.to_csv(self.data.test_data,header=True,index=False)
            
            
            
            return(
        
                train_data,
                test_data
        
            )
                       
            
        except Exception as e:
            
            raise e
            
        
Config_object = Data_Ingestion()

obj_Data_transformation = Data_Transformation()

train_data , test_data = Config_object.Data_ingestion_implimentation()

train_arr , test_arr = obj_Data_transformation.transforming_data(train_data=train_data,test_data=test_data)

trainig_obj = Initialisation()
trainig_obj.data_training(train_arr=train_arr, test_arr= test_arr)



print("Successful")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
    
        
    