import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 &Blueberry Oatmeal')
streamlit.text('🥗 Kale,spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-boiled free range egg')
streamlit.text('🥑 Avocado Toast')

streamlit.header('🍌🍓Build Your Own Fruit Smoothie 🥝🍇')

import pandas
myfruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:",list(myfruit_list.index))

streamlit.dataframe(myfruit_list)
