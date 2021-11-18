# We now need the json library so we can load and export json data  
from flask import Flask, request,jsonify
import joblib
import pandas as pd
import json
import numpy as np
import pickle
app = Flask(__name__)


@app.route('/')
def index():
    return 'App funcionando!'

@app.route('/prediction', methods=['POST'])
def predict():
    #print(request.authorization["username"]) 
    #print(request.authorization["password"])
    # BASIC AUTH
    # esta vez he puesto la contraseña en texto plano. Pero estas pueden
    # ser guardadas como variables de ambiente como buena practica.
    # o consultar un registro en una base de datos con las contraseñas encriptadas con hash
    if (request.authorization["username"] == 'cristobal_quezada') & (request.authorization["password"] == 'tenpo'):
        data = request.get_json()
        #print(data)
        print('ejecutando prediccion')
        #f = open('datos_prueba.json',)
     
        # returns JSON object as
        # a dictionary
        df_data = pd.DataFrame(data)
        #print(df_data)
        columnas = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2',
           'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
           'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
           'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
        
        df_data = df_data[columnas]
        predicts = model.predict(df_data)
        prediction = np.array2string(predicts)
        output = jsonify(prediction)
    
    else:
        output = 'Usuario incorrecto'
    # 
    return output

           

if __name__ == '__main__':
    print('Vamos a ejecutar la API')
    print(joblib.__version__)
    print('pickle',pickle.format_version)
    model = joblib.load('modelo_default_final.pkl')
    app.run(debug=True, host='0.0.0.0')
    
    
    
    
