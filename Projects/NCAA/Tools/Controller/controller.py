import csv
import requests
from bs4 import BeautifulSoup

class Data_Controller:
	def __init__(self, url):
		self.url = url

	def scrape_data(self):
	    response = requests.get(self.url, timeout=10)
	    soup = BeautifulSoup(response.content, 'html.parser')

	    table = soup.find_all('table')[0]

	    rows = table.select('tbody > tr')

	    header = [th.text.rstrip() for th in rows[0].find_all('th')]

	    with open('/home/human/NCAA/SRC/Data/CSV/Stats/ncaa_2017.csv', 'w') as csv_file:
	        writer = csv.writer(csv_file)
	        writer.writerow(header)
	        for row in rows[1:]:
	            data = [th.text.rstrip() for th in row.find_all('td')]
	            writer.writerow(data)

	def scrape_records(self):
	    response = requests.get(self.url, timeout=10)
	    soup = BeautifulSoup(response.content, 'html.parser')

	    table = soup.find_all('table')[1]

	    rows = table.select('tbody > tr')

	    header = [th.text.rstrip() for th in rows[0].find_all('th')]

	    with open('/home/human/NCAA/SRC/Data/CSV/Records/ncaa_2019_record.csv', 'w') as csv_file:
	        writer = csv.writer(csv_file)
	        writer.writerow(header)
	        for row in rows[1:]:
	            data = [th.text.rstrip() for th in row.find_all('td')]
	            writer.writerow(data)


if __name__=="__main__":
    url = "https://www.sports-reference.com/cbb/schools/abilene-christian/2019-schedule.html"
    a = Data_Controller(url)
    a.scrape_records()