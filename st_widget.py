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
'Select Box'
cities = ['London', 'Berlin', 'Paris', 'Madrid']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You live in {city}')

st.divider()

# SLIDER
'Slider'
x = st.slider('x', value=15, min_value=5, max_value=100, step=5)
st.write(f'x is {x}')

st.divider()

# FILE UPLOADER
'Upload File'
uploaded_file = st.file_uploader('Upload a file:', type=['txt', 'csv', 'xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)