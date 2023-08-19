import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://www.espncricinfo.com/series/indian-premire-league-2022-1298423/points-table-standings"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

teams = soup.find_all('span', class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.find_all('td', class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")

team_data = []

for team, win in zip(teams, wins):
    team_name = team.text.strip()
    wins_count = win.text.strip()

    team_dict = {
        'Team Name': team_name,
        'Wins': wins_count
    }

    team_data.append(team_dict)

# Using tabulate to display the data
table_headers = ['Team Name', 'Wins']
table_data = [[entry['Team Name'], entry['Wins']] for entry in team_data]

table = tabulate(table_data, headers=table_headers, tablefmt='grid')
print(table)

# If you want to access individual team data, you can do so like this:
# for entry in team_data:
#     print("Team:", entry['team_name'])
#     print("Wins:", entry['wins'])
#     print("------------")


# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.espncricinfo.com/series/indian-premire-league-2022-1298423/points-table-standings"
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# teams = soup.find_all('span', class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
# wins = soup.find_all('td', class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")
#
# for team in teams:
#     title = team.text.strip()
#     print(title)
#
# print(",,,,,,,,,,,,,,,,,")
#
# for win in wins:
#     num = win.text.strip()
#     print(num)
#
