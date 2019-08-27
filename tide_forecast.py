import re
import requests as r
import time
import pandas as pd
from bs4 import BeautifulSoup as bsoup

class TideForecastScraper:
  def __init__(self, name):
    self.name = name
    self.base_url = 'https://www.tide-forecast.com'
    self.max_tries = 5 # must be more than 0

  def getHTML(self):
    formatted_name = re.sub('[^a-zA-Z0-9 \n\.]', '', self.name).replace(' ','-')
    url = '{}/locations/{}/tides/latest'.format(self.base_url,formatted_name)
    page = self.make_request(url)
    if isinstance(page,TideForecastPage):
      return page
    formatted_name = re.sub('[^a-zA-Z0-9 \n\.]', '', self.name.split(',')[0]).replace(' ','-')
    url = '{}/locations/{}/tides/latest'.format(self.base_url,formatted_name)
    page = self.make_request(url)
    if isinstance(page,TideForecastPage):
      return page
    else:
      raise Exception("Could not load page for {}".format(self.name))

  def make_request(self,url):
    tries = 0
    response = r.get(url)
    while not response.ok and tries < self.max_tries:
      tries +=1
      response = r.get(url)
      time.sleep(1)

    if tries==self.max_tries:
      return False

    return TideForecastPage(response.content)


class TideForecastPage:
  def __init__(self, html):
    self.html = html

  def get_tide_table(self):

    soup = bsoup(self.html,'html5lib')

    table = soup.findAll("table", {"class": "tide-table"})[0]

    all_records =[]
    columns = ['time','timezone','level_metric','level','moonrise']
    for r, row in enumerate(table.find_all('tr')):
        date_holder = row.find_all('th')

        if len(date_holder) > 0:
          date = date_holder[0].contents[0].strip()
        record = {}
        record['date'] = date
        all_column_data = row.find_all('td')
        for c, column in enumerate(all_column_data):
            column_data = all_column_data[c].contents
            if columns[c] == 'level' and len(column_data) > 0:
              record[columns[c]] = column_data[1].contents[0].strip()
            elif len(column_data) > 0:
              record[columns[c]] = all_column_data[c].contents[0].strip()
        all_records.append(record)

    self.df = pd.DataFrame.from_records(all_records)
    return self.df

