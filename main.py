from data_sources import datasets
from tide_forecast import TideForecastScraper, TideForecastPage
import os

if not os.path.exists('results'):
  os.mkdir('results')

#This will store results to print line by line
low_tides = []

for dataset, dataset_attrs in datasets.items():

    #Only run datasets for sites we configure
    if dataset_attrs['run']:

      #Add site name to results
      low_tides += [dataset]

      #Get HTML page for the site
      scraper = TideForecastScraper(dataset)
      page = scraper.getHTML()

      #Save tide dataframe for checking results later
      page.tide_df.to_csv('results/{}.csv'.format(dataset))

      #Get just the dataframe filtered to low tides in daylight hours
      df = page.get_daylight_lowtide_table()

      #Add low tide text to results
      low_tides += df.apply(lambda x: "     {} {} ({})    {}".format( x.date, x.time,x.timezone, x.level), axis =1).to_list()

#Print and save results
result_str = '\n'.join(low_tides)
print(result_str)

with open('results/low_tides.txt','w+') as f:
  f.write(result_str)


