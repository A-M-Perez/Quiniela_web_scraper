# Argentinean "Quiniela"

Quiniela .

## Project objective

This project aims to build a web scraper, using Python with BeautifulSoup, to fetch historical data Quiniela's (lottery) numbers in Argentina.

## Libraries used

- urllib
- BeautifulSoup
- ssl
- csv
- date / timedelta

## Data dictionary (scraped data)

- ***date***: This field contains the date in which the lottery took place. Values can be duplicated, each for a different Quiniela, Period, and Result position. Values should of type DATE.

- ***quiniela***: This field contains the name of the "Quiniela" (lottery), usually referring to the province in which it took place, or "nacional", meaning nation wide. Values can be duplicated, since the same lottery encompasses different dates, Periods, and results. Values are of type TEXT. See possible values in the scraper file's comments.

- ***period***: This field contains the name of the period (time of the day) in which the lottery took place. Values can be duplicated since periods repeat in different dates. Possible values are "primera" (earliest in the morning), "matutina" (morning), "vespertina" (afternoon), "nocturna" (night). Values are of type TEXT.

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

.

## Final considerations

.