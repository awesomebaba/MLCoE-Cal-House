import pickle
import streamlit as st

#Loading Model Here
model = pickle.load(open('reg.pkl', 'rb'))

#Making Streamlit Widgets
name = st.text_area(label="Your Name")
p = st.text_area(label="Longitude")
g = st.text_area(label="Latitude")
bp = st.text_area(label="Housing Median Age	")
stn = st.text_area(label="Total Rooms")
i = st.text_area(label="Total Bedrooms")
bmi = st.text_area(label="Population")
dpf = st.text_area(label="Households")
a = st.text_area(label="Median Income")
op = st.selectbox("Ocean Proximity",('<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'))

if op == '<1H OCEAN':
    opn = 1
elif op == 'INLAND':
    opn = 2
elif op == 'NEAR OCEAN':
    opn = 3
elif op == 'NEAR BAY':
    opn = 4
elif op == 'ISLAND':
    opn = 5


try:
    if st.button("Check"):
        y_pred = model.predict([[float(p), float(g), float(bp), float(stn), float(i), float(bmi), float(dpf), float(a), float(opn)]])
        y_pred = float(y_pred)
        st.markdown("### Results")
        st.write("Price Of the House Is :- ", y_pred)

except:
    st.write("### First Enter Details")