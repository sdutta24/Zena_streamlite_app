import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')
#Connect to snowflake
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=mycnx.cursor()
