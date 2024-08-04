import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

loaded_model = pickle.load(open(r'C:\Users\gauth\Desktop\Gautham\Projects\Parkinson_Disease_Detection\trained_model.sav','rb'))

def parkinson_prediction(input_data):
    sc = StandardScaler()
    input_array = np.asarray(input_data)
    input_reshape = input_array.reshape(1,-1)
    input_sc = sc.fit_transform(input_reshape)
    #input_sc = sc.transform(input_reshape)
    prediction = loaded_model.predict(input_sc)
    if prediction[0] == 0:
        return "Person doesnt have parkinson"
    else:
        return "Person has perkinson"

def main():
    st.title("Parkinson Prediction Webapp")

    FoHz = st.text_input("Enter value of MDVP_Fo(Hz)")
    FhiHz = st.text_input("Enter value of MDVP_Fhi(Hz)")
    FloHz = st.text_input("Enter value of MDVP_Flo(Hz)")
    Jitter = st.text_input("Enter value of MDVP_Jitter(%)")
    Abs = st.text_input("Enter value of MDVP_Jitter(Abs)")
    RAP = st.text_input("Enter value of MDVP_RAP")
    PPQ = st.text_input("Enter value of MDVP_PPQ")
    DDP = st.text_input("Enter value of MDVP_Jitter_DDP")
    Shimmer = st.text_input("Enter value of MDVP_Shimmer")
    dB = st.text_input("Enter value of MDVP_Shimmer(dB)")
    APQ3 = st.text_input("Enter value of Shimmer_APQ3")
    APQ5 = st.text_input("Enter value of Shimmer_APQ5")
    APQ = st.text_input("Enter value of MDVP_APQ")
    DDA = st.text_input("Enter value of Shimmer_DDA")
    NHR = st.text_input("Enter value of NHR")
    HNR = st.text_input("Enter value of HNR")
    RDPE = st.text_input("Enter value of RPDE")
    DFA = st.text_input("Enter value of DFA")
    spread1 = st.text_input("Enter value of spread1")
    spread2 = st.text_input("Enter value of spread2")
    D2 = st.text_input("Enter value of D2")
    PPE = st.text_input("Enter value of PPE")

    diagnosis = ''

    if st.button('Parkinson Test Result'):
        diagnosis = parkinson_prediction([FoHz,FhiHz,FloHz,Jitter,Abs,RAP,PPQ,DDP,Shimmer,dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RDPE,DFA,spread1,spread2,D2,PPE])

    st.success(diagnosis)
    

if __name__ == '__main__':
    main()
