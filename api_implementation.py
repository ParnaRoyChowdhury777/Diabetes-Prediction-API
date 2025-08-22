# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 01:16:58 2025

@author: ASUS
"""

import json
import requests

url = 'https://4e1b25b62c8f.ngrok-free.app/diabetes_prediction'



input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)