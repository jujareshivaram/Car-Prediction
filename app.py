# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:31:51 2021

@author: Jujare Thejasvi
"""
from flask import Flask, render_template, request
import jsonify
import pickle
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#filename="random_forest_regression_model.pkl"
#file=open(filename, "rb")
#model=pickle.load(file)
#try:
model=pickle.load(open('random_forest_regression_model.pkl','rb'))
#except EOFError as e:
  #  handle_error(e)
#def pickle_read():
 #  with open("random_forest_regresson_model.pkl", "rb") as pickle_set:
  #     try:
   #        model = pickle.load(pickle_set)
    #   except EOFError as e:
     #    handle_error(e)


    
                    
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to= StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
   Fuel_Type_Diesel=0
   if request.method == 'POST':
       Year = int(request.form['Year'])
       Present_Price = float(request.form['Present_Price'])
       Kms_Driven = int(request.form['Kms_Driven'])
       Owner = int(request.form['Owner'])
       Year = 2020-Year
       Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
       if(Fuel_Type_Petrol=='Petrol'):
           Fuel_Type_Petrol = 1
           Fuel_Type_Diesel = 0
       elif(Fuel_Type_Petrol=='Diesel'):
           Fuel_Type_Petrol = 0
           Fuel_Type_Diesel = 1
       else:
           Fuel_Type_Petrol=0
           Fuel_Type_Diesel=0
       Seller_Type_Individual = request.form['seller_Type_Individual']
       if(Seller_Type_Individual == 'Individual'):
           Seller_Type_Individual = 1
       else:
           Seller_Type_Individual = 0
       Transmission_Manual=request.form['Transmission_Manual']
       if(Transmission_Manual == 'Manual'):
          Transmission_Manual = 1
       else:
          Transmission_Manual = 0
    
       prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
       output=round(prediction[0],2)
       
       if output<0:
           return render_template('index.html', Prediction_text = "Sorry you cannot sell this car")
       else:
           return render_template('index.html', Prediction_text = "You can sell this car at {}".format(output))
       
   else:
         return render_template('index.html')
     
if __name__=="__main__":
    app.run(debug=True)