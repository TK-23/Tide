from data_sources import datasets
from tide_forecast import TideForecastScraper, TideForecastPage

low_tides = []

for dataset, dataset_attrs in datasets.items():
    if dataset_attrs['run']:
      low_tides += [dataset]
      scraper = TideForecastScraper(dataset)
      page = scraper.getHTML()
      df = page.get_daylight_lowtide_table()
      low_tides += df.apply(lambda x: "     {} {} ({})    {}".format( x.date, x.time,x.timezone, x.level), axis =1).to_list()

result_str = '\n'.join(low_tides)
print(result_str)
with open('low_tides.txt','w+') as f:
  f.write(result_str)


