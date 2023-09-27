import pandas as pd
import pickle

import os
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

from sklearn.svm import SVC

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import r2_score

from utils import save_file

class Training_Configure:
    
    pred_model_path = os.path.join("data_files","predict.pkl")
    
    
class Initialisation:
    
    def __init__(self):
        
        self.best_model = Training_Configure()  
        
        
    def model_configure(self):
        
        models = {
        
            "LogisticRegression":LogisticRegression(),
            "DecisionTreeClassifier":DecisionTreeClassifier(),
          "RandomForestClassifier":RandomForestClassifier(),
            "SVM":SVC(),
            "GaussianNB":GaussianNB(),
            "KNeighborsClassifier":KNeighborsClassifier(n_neighbors=3)
             
        
        }
        
        #hyper parameter tuning
        
        parameters = {
        
            #logistic regression
            "LogisticRegression":{                       
            
            },
             #knc
            "KNeighborsClassifier":{ "weights":['uniform', 'distance'],
            "metric" :['euclidean', 'manhattan', 'minkowski'],
            "n_neighbors":range(1,21,2)
                     
            },
            
            #svm
            "SVM":{ "kernel" : ['poly', 'rbf', 'sigmoid'],
            "C": [50, 10, 1.0, 0.1, 0.01],        
            
            },
            
            #rf
            "RandomForestClassifier":{"n_estimators" :[10, 100, 1000],
            "max_features" : ['sqrt', 'log2']            
            
            },
            
            #dtc
            "DecisionTreeClassifier":{'criterion': ["gini", "entropy"]        
            
            },
            
         "GaussianNB": {
    
         }        
        
        
        }
        
        return (
        models,
        parameters)
        
    def data_training(self,train_arr,test_arr):
        
        try:
            
            my_dict = { }
            
            train_arr_data = train_arr[:,:-1]
            target_train_data = train_arr[:,-1]
            
            test_arr_data = test_arr[:,:-1]
            target_test_data = test_arr[:,-1]
            
            model_obj, parameters = self.model_configure()
            
            for i in range(len(model_obj.keys())):
                
                estimator = list(model_obj.values())[i]
                parameter = parameters[list(model_obj.keys())[i]]
                
                #grid search cv
                cv = GridSearchCV(estimator=estimator,param_grid= parameter,cv = 3)
                
                cv.fit(train_arr_data,target_train_data)
                
                predictions= cv.predict(test_arr_data)
                
                accuracy = accuracy_score(target_test_data,predictions)
                
                
                my_dict[list(model_obj.keys())[i]] = accuracy
                
            best_model_obj = max(my_dict.keys())
            
            best_model = model_obj[best_model_obj]
            
            main_prediction = best_model.fit(train_arr_data,target_train_data)
            
            save_file(
            
            best_model,
            self.best_model.pred_model_path
            )
            
            return best_model
                
                
         
                
                
                
            
                         
        except Exception as e:
            raise e