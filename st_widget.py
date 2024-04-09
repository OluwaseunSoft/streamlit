import streamlit as st
import pandas as pd

#Text input
name = st.text_input('Name')
if name:
    st.write(f'Hello {name}!')


x = st.number_input('Enter a number', min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')

st.divider()

#Button
