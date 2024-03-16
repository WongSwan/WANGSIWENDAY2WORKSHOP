import streamlit as st
from joblib import load

model = load('spam_detector_model.joblib')

st.title('Spam Detection')

message = st.text_area("Input the email content:")

if st.button('TEST'):

    prediction = model.predict([message])[0]

    if prediction == 0:
        st.success('This is not spam.')
    else:
        st.error('This is spam。')
