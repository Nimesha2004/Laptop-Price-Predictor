import streamlit as st
import pickle
import pandas as pd 

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

try:
    pipe=pickle.load(open('laptop_pipe.pkl','rb'))
except FileNotFoundError:
    st.error("❌ Error: 'laptop_pipe.pkl'Unable to find.")
    st.stop()

st.title("💻 Laptop Price Predictor")
st.write("Enter the price of the laptop and get an estimated price")
st.markdown("----")

col1,col2 = st.columns (2)

with col1:
    company = st. selectbox ('Brand ',['Hp', 'Asus', 'Dell', 'Lenovo', 'Apple', 'Acer', 'MSI'])
    cpu= st.selectbox('Processor', ['Intel Core i3', 'Intel Core i7', 'Intel Core i9','AMD Ryzen 3', 'AMD  Ryzen 5','AMD  Ryzen 7','M1','M2','M3'])
    ram = st.selectbox('RAM', [4,8,16,32])
with col2:
    storage = st.selectbox('Storage Type', ['256GB SSD', '512GB SSD','1TB SSD','1TB HDD'])
    opsys = st.selectbox('Operating System',['Windows 11', 'Windows 10', 'mscOS', 'Ubuntu', 'No OS'])
    weight = st.number_input('Weight (kg)',min_value=1.0,max_value=4.0,value=1.7,step=0.1)

st.markdown("-----")

if st.button('💰 Predict Laptop Price', use_container_width=True):
    input_data = pd.DataFrame([[company,cpu,ram,storage,opsys,weight]],
                             columns=['Company', 'CPU', 'Ram', 'Storage', 'OpSys', 'Weight'])
    predicted_price = pipe.predict(input_data)[0]
    st.success(f"### Estimated Price : LKR {predicted_price:,.2f}")
