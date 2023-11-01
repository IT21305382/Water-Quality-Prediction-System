import streamlit as st
import joblib
import numpy as np
import pandas as pd

model=joblib.load('DTmodel.pkl')

col1, col2,col3= st.columns(3)
with col1:
# Add a custom logo image and adjust its size
    st.image('logo3.png', width=200)  # Replace 'your_logo.png' with the path to your image
with col2:
    st.title("")
    st.title("HydroAnalyzer")
    st.write("Water Quality Predition System")
st.write("Please, fill measurements(in miligrams) relevant to your sample below:")

col1, col2, col3, col4 = st.columns(4)
input_labels=["aluminium", "ammonia", "arsenic", "barium", "cadmium", "chloramine", "chromium", "copper", "flouride", "bacteria", "viruses", 
      "lead", "nitrates", "nitrites", "mercury", "perchlorate", "radium", "selenium", "silver", "uranium"]

input_vals=[]


    
col1, col2, col3, col4= st.columns(4)

    # with st.form("elements"):
        
with col1:
    for label in input_labels[0:5]:
        value = st.number_input(f"{label}:", step=0.1)
        input_vals.append(value)
        
with col2:
    for label in input_labels[5:10]:
        value = st.number_input(f"{label}:", step=0.1)
        input_vals.append(value)
        
with col3:
    for label in input_labels[10:15]:
        value = st.number_input(f"{label}:", step=0.1)
        input_vals.append(value)
    
with col4:
    for label in input_labels[15:21]:
        value = st.number_input(f"{label}:", step=0.1)
        input_vals.append(value)
            
submitted = st.button("Test")
            
if submitted:
    print(input_vals)
    input_data = np.array(input_vals)
    pred=model.predict(input_data.reshape(1, -1)) 
    print(pred)
            
            
    if int(pred[0])==1:
        st.subheader("This sample is safe.")
    else:
        st.subheader("This is an unsafe sample")
        
    dataframe=pd.DataFrame({'Content':input_labels, 'Amount':input_vals})
    st.bar_chart(data=dataframe, x="Content", y=None, color=None, width=0, height=0, use_container_width=True)

    