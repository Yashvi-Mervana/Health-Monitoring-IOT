import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('remodel.sav', 'rb'))

#create function

def health(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    input_data_f=input_data_reshaped
    predictions = loaded_model.predict(input_data_f)
    if predictions==['Normal']:
        return "Your Vital Signs Are Normal"
    else:
        return "Your Vital Signs are Abnormal"
  

def main():

    #title of webpage
    st.title("VITAL SIGNS TRACKER")

    #getting input data
    HR=st.text_input("Heart Rate (Beats Per Minute)")
    RESP= st.text_input("Respiratory Rate (Breaths Per Minute)")
    SPO2= st.text_input("SPO2 (in %)")
    TEMP=st.text_input("Body Temperature (in °C)")

    #code for prediction
    diagnosis= ""

    #button for pred
    if st.button("Submit"):
        diagnosis = health([HR,RESP,SPO2,TEMP])

    if "Abnormal" in diagnosis:
        st.error(diagnosis)
    else:
        st.success(diagnosis)

    #st.success(diagnosis)


if __name__ == "__main__":
    main()