from data_sources import datasets
from tide_forecast import TideForecastScraper, TideForecastPage


for dataset, dataset_attrs in datasets.items():
    if dataset_attrs['run']:
      scraper = TideForecastScraper(dataset)
      page = scraper.getHTML()
      df = page.get_tide_table()
      df.to_csv('{}.csv'.format(dataset))

