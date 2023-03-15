# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:05:10 2023
@author: Khutso9
"""
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('Diabetes_Model.sav','rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction =loaded_model.predict(np.array(input_data_reshaped))
    
    print(prediction)
    
    if (prediction[0] == 0):
        print('The person is not Diabetic')
    else:
        print('The person is Diabetic!!!')
def main():
    
    st.title('Diabetes Prediction Web App')
    
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Body Mass index value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age Of the Person')
   
    #Prediction
    diagnose = ''
    
    if st.button('Diabetes Test Results'):
        diagnose = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnose)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    