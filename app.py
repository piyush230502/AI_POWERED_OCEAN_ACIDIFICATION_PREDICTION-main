from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 



@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Treatment_Temperature =float(request.form['Treatment-Temperature'])
            Temp =float(request.form['Temp'])
            Sal =float(request.form['Sal'])
            pH =float(request.form['pH'])
            TA =float(request.form['TA'])
            Nitrite =float(request.form['Nitrite'])
            Nitrate =float(request.form['Nitrate'])
            Ammonium =float(request.form['Ammonium'])
            Silicate =float(request.form['Silicate'])
            Phosphate =float(request.form['Phosphate'])
            DIC =float(request.form['DIC'])
            pCO2 =float(request.form['pCO2'])
            Omega_Cal =float(request.form['Omega-Cal'])
            Omega_Arag =float(request.form['Omega-Arag'])
            Bicarbonate_ion =float(request.form['Bicarbonate-ion'])
            Carbonate_ion =float(request.form['Carbonate-ion'])
            CO2 =float(request.form['CO2'])
       
         
            data = [Treatment_Temperature, Temp, Sal, pH, TA, Nitrite,Nitrate, Ammonium, Silicate, Phosphate, DIC, pCO2,Omega_Cal, Omega_Arag, Bicarbonate_ion, Carbonate_ion, CO2]
            data = np.array(data).reshape(1, 17)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')
    



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)
