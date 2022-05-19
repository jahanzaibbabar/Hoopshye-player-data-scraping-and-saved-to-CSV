from selenium import webdriver 

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

# print("\n\n", players_list)
# print("\n\n", salaries_list)

for x in range(10):
    print("\n\t", players_list[x], "\t\t", salaries_list[x])
