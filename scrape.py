import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://www.w3schools.com/html/html_tables.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'id': 'customers'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./customers.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Company", "Contact", "Country"])
writer.writerows(list_of_rows)