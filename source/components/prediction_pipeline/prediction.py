import pandas as pd



class Data_model_Config:
    pass
    
    
class Model_prediction_data:
    
    def __init__(self,
    
        gender,
        marriage,
        education,
        selfemployment,
        income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area,
        dependents 
        ):
        
        try:
            
            self.gender = gender,
            self.marriage = marriage,
            self.education = education,
            self.selfemployment = selfemployment,
            self.income = income,
            self.coapplicant_income = coapplicant_income,
            self.loan_amount = loan_amount,
            self.loan_amount_term = loan_amount_term,
            self.credit_history = credit_history,
            self.property_area = property_area,
            self.dependents = dependents
            
            
        except Exception as e:
            raise e
        
    def data_frame_object(self):
        try:
            #creating a data frame
            my_dict = {
            
            "gender":str(self.gender),
            "marriage":str(self.marriage),
            "edication":str(self.education),
            "employment":str(self.selfemployment),
            "income":self.income,
            "coapplicant_income":self.coapplicant_income,
            "loan_amount":self.loan_amount,
            "loan_mount_term":self.loan_amount_term,
            "credit_history":self.credit_history,
            "property_area":str(self.property_area),
            "dependents":str(self.dependents)
            }
            
            
            
            data = pd.DataFrame(my_dict,index=[0])
            return data
            
 
            
            
        except Exception as e:
            
            raise e
            
        
        
        
        
        
    
    
    
  
    
        
        