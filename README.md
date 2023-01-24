# Argentinean "Quiniela"

One of the most popular Argentinean lotteries is called "Quiniela", where people can bet from anywhere in the country and takes place four times a day. People can bet on any number, at any position (1 to 20), for a specific period of the day (4 of them), province in which the lottery takes place, and number of digits.

For example, one person can place a bet of $10 to the number 1234, position 1, Quiniela nacional at the period "vespertina". Another example, could be the exact same, but only betting at the number 12.

The "Quiniela" pays as follows (for position 1):
- 4 digits right -right to left-: 3.500 times what has been bet.
- 3 digits right -right to left-: 600 times what has been bet.
- 2 digits right -right to left-: 70 times what has been bet.
- 1 digit right -right to left-: 7 times what has been bet.

## Project objective

This project aims to build a web scraper, using Python with BeautifulSoup, to fetch historical data Quiniela's (lottery) numbers in Argentina. This data can be used to analyze patterns and predict the Quiniela's results.

## Libraries used

- urllib
- BeautifulSoup
- ssl
- csv
- date / timedelta

## Data dictionary (scraped data)

- ***date***: This field contains the date in which the lottery took place. Values can be duplicated, each for a different Quiniela, Period, and Result position. Values should of type DATE.

- ***quiniela***: This field contains the name of the "Quiniela" (lottery), usually referring to the province in which it took place, or "nacional", meaning nation wide. Values can be duplicated, since the same lottery encompasses different dates, Periods, and results. Values are of type TEXT. See possible values in the scraper file's comments.

- ***period***: This field contains the name of the period (time of the day) in which the lottery took place. Values can be duplicated since periods repeat in different dates. Possible values are "primera" (earliest in the morning), "matutina" (early afternoon), "vespertina" (afternoon), "nocturna" (night). Values are of type TEXT.

- ***position***: This field contains the position number in which the result was drawn. There are 20 -4 digit- numbers drawn in each Quiniela, Period and date. Values can be duplicated since every Quiniela and Period have the same number of positions. Values are of type NUMBER.

- ***result***: This field contains the result for the specific lottery and position. Values cannot be duplicated for the same Quiniela, Period and date. Values are of type NUMBER and should integers of 4 digits.

> Source : https://www.nacionalloteria.com/argentina/quinielas.php


## Repository overview / structure

├── README.md\
├── Quiniela_stats_scraper.py (scrapes Quiniela's historical data)\
├── data (scraped data results)\
&emsp;&emsp;├── buenos-aires-primera.csv\
&emsp;&emsp;├── buenos-aires-matutina.csv\
&emsp;&emsp;├── buenos-aires-vespertina.csv\
&emsp;&emsp;├── buenos-aires-nocturna.csv\
&emsp;&emsp;├── nacional-primera.csv\
&emsp;&emsp;├── nacional-matutina.csv\
&emsp;&emsp;├── nacional-vespertina.csv\
&emsp;&emsp;├── nacional-nocturna.csv


## Running instructions

>*DO NOT FORGET to check the https://www.nacionalloteria.com/robots.txt file to ensure compliance with the website's search engine crawlers policy*

To test or run this script, please:

- Clone the repository or download the file "Quiniela_stats_scraper.py"
- Import the file "Quiniela_stats_scraper.py" to your favourite integrated development environment (IDE) supporting Python
- Edit the arrays for "Quinielas" and "Periods" to fit your objectives of scraped data
- Run the entire script

## How this project helped me grow:

The main challenge I faced with this project, was to think of an efficient way to scrape data from all "Quinielas" and "Periods", exporting it in a way that could be practically used by anyone.

To overcome this, I decided to create a specific file for each of the parameters' combinations, making it easy to modify using arrays.

## Final considerations

This project only aimed at scraping data and was tested with a few "Quinielas", so running it for all available options of "Quinielas" and "Periods" might be really time consuming and prompt errors not encountered with a more limited scope.