import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/yashu/Desktop/ROSP/rosp/remodel.sav', 'rb'))

new_data = [[99.0,19.0,96,35]]
predictions = loaded_model.predict(new_data)
if predictions==['Abnormal']:
    print("Your Vital Signs are Abnormal")
else:
    print("Your Vital Signs are Normal")