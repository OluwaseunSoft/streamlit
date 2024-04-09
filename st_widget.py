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
is_clicked = st.button('Guess What???')
if is_clicked:
    st.write(':ghost:' * 10)


st.divider()

#Checkbox
agree = st.checkbox('TsCs')
if agree:
    'Welcome'

checked = st.checkbox('Continue', value=True)
if checked:
    ':+1:' * 3


df = pd.DataFrame({'Name': ['Anne', 'Maria', 'Douglas'],
                   'Age': [30, 25, 40]})
if st.checkbox('Show data'):
    st.write(df)

#RadioButton
pets = ['cat', 'dog', 'fish', 'turtle']
pet = st.radio('Favorite pet', pets, index=2, key='your_pet')
st.write(f'Your favorite pet: {pet}')
st.write(f'Your favorite pet: {st.session_state.your_pet * 3}')

st.divider()

# SELECTBOXES
cities = ['London', 'Berlin', 'Paris', 'Madrid']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You live in {city}')

st.divider()

