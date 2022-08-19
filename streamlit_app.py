import streamlit

streamlit.title('My Mom´s New Healty Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# variable mit Liste füttern
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# variablenwerte übergeben 
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# vorher: liste einfach anzeigen mti --> streamlit.dataframe(my_fruit_list)
# jetzt aus variable bedienen
streamlit.dataframe(fruits_to_show)

#  Lesson 9: Streamlit - Using APIs & Variables - API Calls in Streamlit
# Let's Call the Fruityvice API from Our Streamlit App!
# We need to bring in another Python package library. This one is called requests. 
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
