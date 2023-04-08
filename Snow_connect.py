

import streamlit as st
import snowflake.connector

# Establishing connection to Snowflake database
conn = snowflake.connector.connect(
    user='manojrayan',
    password='Jmr123#open',
    account='SQBCIFA-DE78525',
    warehouse='COMPUTE_WH',
    database='ECONOMY_DATA_ATLAS',
    schema='ECONOMY',
)

# Creating a cursor to execute SQL statements
cursor = conn.cursor()

# Streamlit app
def main():
    # Title
    st.title("Snowflake Table Explorer")

    # Select table from dropdown
    selected_table = st.selectbox("Select a table", get_table_list())

    # Display table data
    if selected_table:
        cursor.execute(f"SELECT * FROM {selected_table} LIMIT 10")
        results = cursor.fetchall()
        st.write("Query Results:")
        st.table(results)

    # Closing the cursor and connection
    cursor.close()
    conn.close()

# Function to get the list of tables in Snowflake database
def get_table_list():
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    table_list = []
    for table in tables:
        table_list.append(table[1])
    return table_list

if __name__ == '__main__':
    main()