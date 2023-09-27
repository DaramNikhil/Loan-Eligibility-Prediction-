import pickle

def save_file(processor,path):
    
    try:
        with open(path,"wb") as f:
            
            pickle.dump(processor,f)
            
    except Exception as e:
        
        raise e
        
        
    
    