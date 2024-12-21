import pandas as pd 
from bs4 import BeautifulSoup
import requests
import sqlite3

# 
url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = "Movies.db"
table_name = "Top_50"
csv_path = "/home/project/top_50_films.csv"

# Create an empty data frame with the specific schema
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

# Loading the webpage for Webscraping
html_page = requests.get(url).text
data= BeautifulSoup(html_page, "html.parser")

# Extract the information from the web page
tables = data.find_all("tbody")
rows = tables[0].find_all("tr")

# Iterate over the rows and load the information in a data frame
for row in rows:
    if count < 50:
        cell = row.find_all("td")
        if len(cell)!= 0:
            data_dict = {"Average Rank": cell[0].contents[0],
                        "Film": cell[1].contents[0],
                        "Year": cell[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index = True)
            count+=1
    else: 
        break

print(df)        

# Save the data in a csv file
df.to_csv(csv_path)

# Store the data in a database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists = "replace", index = False)
conn.close
