# ikmanSpider

ikmanSpider is a Python script that uses the Scrapy framework to scrape electronics ads from the ikman.lk website.

## Installation

1. Clone the repository to your local machine.
2. Install Scrapy using pip: `pip install scrapy`

## Usage

1. Open a terminal and navigate to the directory containing the ikmanSpider.py file.
2. Run the spider using the command: `scrapy crawl ikman -o output.json`
3. The spider will start scraping the website and will output the extracted data to a JSON file named "output.json".

## Configuration

The spider is configured to scrape the first 5 pages of the electronics ads section of the ikman.lk website. You can modify the `start_urls` variable to change the starting pages, and the `if` statement in the `parse` method to change the maximum number of pages to scrape.


