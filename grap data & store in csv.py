
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://hoopshype.com/salaries/players/")

players = driver.find_elements_by_xpath('//td[@class="name"]')

players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)


salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')

salaries_list = list()
for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)

ranks = driver.find_elements_by_xpath('//td[@class="rank"]')
ranks_list = list()
for r in range(len(ranks)):
    ranks_list.append(ranks[r].text)

# # output
# for x in range(len(players_list)):
#     print("\n\t", ranks_list[x], "\t", players_list[x], "\t\t", salaries_list[x])

# print("\n\n", len(players_list))
# print("\n\n", len(salaries_list))

data_tuple = list(zip(players_list[1:], salaries_list[1:]))
df = pd.DataFrame(data_tuple, columns=['Player Name', 'Salary'], index=ranks_list[1:])

print(df)

filename = 'players_data.csv'
df.to_csv(filename)
