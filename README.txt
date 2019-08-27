#Prequisites

  1. Download conda if you don't have it already (https://www.anaconda.com/distribution/)

  2. Install and activate the environment:
         $ conda env update -f environment.yml;
         $ conda activate tide

      Note: Alternately, you can run outside this Conda environment so long as you have Python 3, Pandas=0.25.0 and beautifulsoup4=4.8.0

#The Script
  Set your working directory to this folder.

  Sites for which low tide data will be parsed are located in data_sources.py. Add to this dictionary to include more sites, or set 'run' to False to exclude a site from running.

  To download the HTML page for each site, parse the tide table and filter daylight low tide event, run (from this working directory):

        $ python main.py

  This script will create csv's in a ‘results’ folder for each site of the raw tide table data for QA. It will also print daylight low tide events to the screen, and write daylight low tide events to a text file in the results folder called 'low_tides.txt'.
