Prequisites

  1. Download conda if you don't have it already (https://www.anaconda.com/distribution/)

  2. Install and Activate the environment
      ```
          conda env update -f whatever.yml;
          conda activate tide
      ```
      Note: You can run outside this env so long as you have Python 3, Pandas 0.25.0 and beautifulsoup4 4.8.0

The Script
  Set your working directory to this folder.

  Sites for which low tide data will be parsed are located in data_sources.py. Add to this dictionary to include more sites, or set 'run' to False to exclude a site from running.

  Run the HTML page download, tide table parsing and filter of daylight low tide events with:

  ```
  python main.py

  ```

  This will create csv's for each site of the raw tide table data, print daylight lowtide events to the screen, and write daylight low tide events to a text file called 'low_tides.txt' in the working directory.
