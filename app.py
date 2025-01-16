import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

#read data
df = pd.read_csv("pipes.csv")

# train model
model = LinearRegression()
x = df[["diameter"]]
y = df[["price"]]

model.fit(x,y)

# app web
st.title("Pipe price prediction")
st.divider()
st.write("This app predicts the price of pipes")
st.write("Enter the diameter of the pipe in mm to show the price:")

diameter = st.number_input("Diameter", min_value=10, max_value=30, step=1, value=10)

if diameter:
    price = model.predict([[diameter]])[0][0]
    st.write(f"The predicted price is: ${price:.2f}")


