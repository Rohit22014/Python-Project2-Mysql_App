import mysql.connector

con = mysql.connector.connect(
host="localhost",
user ="root",
password ="",
database ="test"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
    else:
        print("No word found!")