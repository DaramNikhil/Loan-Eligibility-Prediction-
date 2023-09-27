from flask import Flask,render_template,url_for,request
import pandas as pd
#from source.components.data_files import processor
#from source.components.data_files import predict
import pickle
from source.components.prediction_pipeline import prediction

app = Flask(__name__,template_folder="templates")

@app.route("/",methods=["POST","GET"])
def home_page():
    
    if request.method == "POST":
        
        gender = str(request.form["Gender"])
        
        marriage = str(request.form["Marriage"])
        
        education = str(request.form["Education"])
        
        selfemployment= str(request.form["selfemployment"])
        
        income = float(request.form["ApplicantIncome"])
        
        coapplicant_income = float(request.form["CoapplicantIncome"])
        
        loan_amount = float(request.form["LoanAmount"])
        
        loan_amount_term = float(request.form["Loan_Amount_Term"])
        
        credit_history = float(request.form["Credict_History"])
        
        property_area = str(request.form["Property_Area"])
        
        dependents = float(request.form["Dependents"])
        
        
        #predictions vals
        df = prediction.Model_prediction_data(
           gender=gender,
           marriage=marriage,
           education=education,
           selfemployment=selfemployment,
           income=income,
           coapplicant_income=coapplicant_income,
           loan_amount=loan_amount,
           loan_amount_term=loan_amount_term,
           credit_history=credit_history,
           property_area=property_area,
           dependents=dependents
           )
           
        data =df.data_frame_object()                  
        
        #preprocessing pickle file
        with open("/storage/emulated/0/loan_eligibility_prediction/source/components/data_files/processor.pkl","rb") as processor:
            
            processor_obj = pickle.load(processor)
            
        #prediction pickle file
        with open("/storage/emulated/0/loan_eligibility_prediction/source/components/data_files/predict.pkl","rb") as predict:
            
            pred_obj = pickle.load(predict)
        
        pre_data = processor_obj.transform(data)
        
        final_pred = pred_obj.predict(pre_data)
        
        return render_template("pred.html",final_pred = final_pred)
        
    else:
        return render_template("display.html")


if __name__ == "__main__":
    
    app.run(debug=True)