import requests
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://native-stats.org/team/86")

print(driver.page_source)

driver.quit()

# rows = []

# def get_cell_text(cell):
#     if cell.span:
#         return cell.span.get_text(strip=True)
#     return cell.get_text(strip=True)

# # Adding the data from the website to our table
# for row in table.tbody.find_all('tr'):
#     columns = row.find_all('td')

#     if columns:
#         rows.append({
#             'Date': get_cell_text(columns[0]),
#             'Competition': get_cell_text(columns[1]),
#             'Match': get_cell_text(columns[2]),
#             'Score': get_cell_text(columns[3]),
#             'odds': get_cell_text(columns[4]),
#             'omv': get_cell_text(columns[5]),
#         })

# df = pd.DataFrame(rows)
# print(df)
