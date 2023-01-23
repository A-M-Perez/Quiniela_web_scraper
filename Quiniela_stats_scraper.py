# Import libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import csv
from datetime import date, timedelta

# Ignore certification validation
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Define arrays of available "Quinielas" and "Periods" to be scraped (all available options included below)
quinielas_list = ['nacional', 'buenos-aires', 'misiones', 'corrientes', 'san-luis', 'mendoza', 'san-juan', 'salta', 'chaco', 'uruguay', 'formosa', 'santa-fe', 'cordoba', 'entre-rios', 'tucuman', 'santiago-del-estero', 'neuquen']
periods_list = ['primera', 'matutina', 'vespertina', 'nocturna']

# Iterate through available "Quinielas", and for each of them, through all available "Periods"
for quiniela_argument in quinielas_list:

    for period_argument in periods_list:

        # Define a range of dates for scraping data within that timeframe (largest date range defined below)
        results_date = date(2014, 10, 31) # Oldest date with data in the website is 2014-11-01 
        end_date = date.today()
        date_delta = timedelta(days=1)

        # Create and set the structure of the file to be exported with scraped data (one file per Quiniela & Period)
        file = open('./data/{}-{}.csv'.format(quiniela_argument, period_argument), 'w', newline='')
        writer = csv.writer(file)
        quiniela_file_headers = ['date', 'quiniela', 'period', 'position', 'result']
        writer.writerow(quiniela_file_headers)

        # Iterate through the date range (one web page per date) to obtain the data
        while results_date <= end_date:
            results_date += date_delta 

            # Set HTML parser
            base_url = 'https://www.nacionalloteria.com/argentina/quiniela-{}.php?del-dia={}&periodo={}'.format(quiniela_argument, results_date, period_argument)
            html = urllib.request.urlopen(base_url, timeout=60, context=ctx).read()
            soup = BeautifulSoup(html, 'lxml')

            # Create array to store individual table rows
            quiniela_file_rows = []
            # Find rows with lottery results
            rows = soup.find_all('td', class_='celNor tacenter')
            
            # Iterate through the lottery results table rows and cells, writing them individually into the CSV file
            try:
                i = 0
                while i < 42: # There are 21 rows with 2 relevant cells per row ("position" & "result")
                    quiniela_file_rows = [results_date.strftime('%Y-%m-%d'), quiniela_argument, period_argument, rows[i].text, rows[i+1].text]
                    i += 2
                    writer.writerow(quiniela_file_rows)
            except:
                continue

        file.close() # Save and close file

exit()

# #UNCOMMENT CODE TO CHECK OUT PAGE HTML
# with open('lottery_numbers_page_template.html', 'wb') as file:
#     file.write(soup.prettify('utf-8'))