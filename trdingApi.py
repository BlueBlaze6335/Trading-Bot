


import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import time
import seaborn as sns

# Connect to MySQL database
cnx = mysql.connector.connect(user='username', password='password',
                              host='localhost', database='database_name')
cursor = cnx.cursor()

# Create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS data (
    Strike	INT,
    CE	INT,
    PE	INT,
    Time STRING
);
"""

cursor.execute(create_table_query)

# Keep running every 1 minute
while True:
    # Load data from Excel file
    data = pd.ExcelFile("D:/tradingFolder/OC (1).xlsx")
    data = pd.read_excel(data,'Sheet4')
    # Insert data into MySQL
    for i in range(len(data)):
        name = data.iloc[i]['16850']
        value = data.iloc[i]['Value']
        insert_query = f"INSERT INTO data (name, value) VALUES ('{name}', {value})"
        cursor.execute(insert_query)

    cnx.commit()

    # Plot the data
    plt.plot(data['TIME'], data['16850C'])
    # p= sns.lineplot(x=data['TIME'], y=data['16850C'],
    #              color='g', data=data)
    plt.plot(data['TIME'], data['16850P'])
    # p= sns.lineplot(x=data['TIME'], y=data['16850C'],
    #              color='g', data=data)
    plt.xticks(rotation=90,fontsize=6)
    # plt.xlabel('Time')
    # plt.ylabel('C value for SP 16850')
    # plt.title('Data')
    plt.show()

    # Wait for 1 minute before running again
    time.sleep(60)



