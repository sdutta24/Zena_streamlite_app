import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')
#Connect to snowflake
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=mycnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
