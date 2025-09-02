import os
from utils.scraping import scrape_data
from utils.file_operations import data_from_csv
from utils.plot import create_plot


if __name__ == "__main__":

    if os.path.exists('data.csv'):
        create_plot(data_from_csv())

    else:
        scrape_data()
        create_plot(data_from_csv())