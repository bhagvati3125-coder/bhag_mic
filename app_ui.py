import streamlit as st
import pickle

model=pickle.load(open("model.pkl","rb"))
st.title("slary prediction app")
exp=st.number_input("Enter Exprience",min_value=0,max_value=50,value=1)


if st.button("Prediction"):
    result=model.predict([[exp]])
    st.write(f"pridected salary:{int(result[0])}")