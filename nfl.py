# -*- coding: utf-8 -*-
"""
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.nfl.com/standings/league/2021/REG"

page = requests.get(url).text

soup = BeautifulSoup(page, "lxml")

table = soup.find("table")

header = [data.text for data in table.find_all("th")]
df = pd.DataFrame(columns = header)

rows = soup.find_all("tr")[1:]
print(rows)

for row in rows:
    first_data = row.find_all("td")[0].find("div", class_="d3-o-club-shortname").text.strip()
    row_texts = [data.text for data in row.find_all("td")[1:]]
    row_texts.insert(0, first_data)
    length = len(df)
    df.loc[length] = row_texts

df.to_csv("C:/Users/swuma/scrapping/nfl.csv")