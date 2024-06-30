Web Scraping with BeautifulSoup and Scrapy
Overview

This project demonstrates how to scrape smartphone listings from the Spacenet.tn website using Scrapy with BeautifulSoup for parsing HTML content. The scraped data is then stored in a CSV file for further analysis or processing.
Requirements

    Python 3.x
    Scrapy
    BeautifulSoup

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/scraping-beautifulsoup.git
cd scraping-beautifulsoup

Install dependencies:

bash

    pip install scrapy beautifulsoup4

Usage

    Run the Scrapy spider:

    Navigate to the project directory and execute:

    bash

    scrapy crawl spacenettn -o spacenet_smartphones.csv

    This command will start the spider (spacenettn) defined in spiders/spacenettn.py and output the scraped data to spacenet_smartphones.csv.

    Inspect the CSV output:

    Once the spider completes scraping, check the spacenet_smartphones.csv file in the project directory. It should contain columns for ad_url, ad_title, ad_price, ad_stocks, ad_website, and date_scrapy.

Spider Implementation Details

The Spider (spacenettnSpider) is configured to start scraping from the URL https://spacenet.tn/13-smartphone-mobile-tunisie. It extracts smartphone listings including title, price, availability, and URL. Pagination is handled to scrape multiple pages.
Example CSV Output

csv

ad_url,ad_title,ad_price,ad_stocks,ad_website,date_scrapy
https://spacenet.tn/smartphone1,Smartphone 1,499 DT,In stock,https://spacenet.tn/13-smartphone-mobile-tunisie,2024-07-01 12:00:00
https://spacenet.tn/smartphone2,Smartphone 2,699 DT,Out of stock,https://spacenet.tn/13-smartphone-mobile-tunisie,2024-07-01 12:00:00
...
