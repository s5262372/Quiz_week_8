import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()
db_years = """
SELECT Year
FROM ClimateData
"""

db_co2 = """
SELECT CO2
FROM ClimateData
"""

db_temp = """
SELECT Temperature
FROM ClimateData
"""

cursor.execute(db_years)
year_results = cursor.fetchall()

cursor.execute(db_co2)
co2_results = cursor.fetchall()

cursor.execute(db_temp)
temp_results = cursor.fetchall()

years = [year for year in year_results]
co2 = [reading for reading in co2_results]
temp = [record for record in temp_results]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
