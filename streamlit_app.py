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
streamlit.header("Fruityvice Fruit Advice!")

# Start Lesson 9: Streamlit - Using APIs & Variables Variables in Streamlit
# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# Ende Lesson 9: Streamlit - Using APIs & Variables Variables in Streamlit


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# streamlit.text(fruityvice_response) # just writes the data to the screen

# Course Lesson 9: Streamlit - Using APIs & Variables - Making the JSON Look Good 
# write your own comment -what does the next line do? show content like a string less readable
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do? show content in a readable table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
streamlit.header("the fruit list contains:")
# streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)


#  Lesson 12: Streamlit, but with Snowflake Added Streamlit Challenge Lab! 
# Allow the end user to add a fruit to the list
# add_my_fruit = ....................

#  Lesson 12: Streamlit, but with Snowflake Added Time to Tidy Up? 
# Write Code to Add Rows to Our Fruit List in Snowflake
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
