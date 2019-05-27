# Importing system module for taking command line arguments.
import sys
if len(sys.argv) < 2:
	print("Command Line Argument isn't supplied!")
	exit(0)

# Import Required Libraries.
from requests_html import HTMLSession


print('Query: ',sys.argv[1])

# Search Query
query = sys.argv[1]

# Original Site.
site = 'https://www.daraz.pk/catalog/'

payload = {'q':query}

# Creating the Session
print('Creating the HTML Sesstion')
session = HTMLSession()

# Requesting the site and waitiing to get the HTML Response back.
print('Requesting the Site information using get method.')
response = session.get(site,params=payload)	# If all wents well Response Code#200 will be sent back.
# getting the html of that page.
print('Response returns successfully!')

print('Response Status Code: ',response.status_code)
print('Response URL: ',response.url)

if response.status_code == 200:
	html = response.html

	print('Rendering the Java Script Code.')
	html.render()

	card_class = 'c3e8SH'
	info_class = 'c3KeDq'

	print('Scrapping the DATA.')

	import csv
	file_name = query + '.csv'
	file = open(file_name, 'w')
	csv_writer = csv.writer(file)
	header = ['Product Name', 'New Price', 'Old Price', 'Discount']
	csv_writer.writerow(header)

	# List all the cards 
	cards = html.find('div.{}'.format(card_class))
	for card in cards:
	    info = card.find('div.{}'.format(info_class), first=True)
	    title = info.find('a', first=True).attrs['title']
	    price = info.find('div.c3gUW0', first=True).text
	    spans = info.find('div.c3lr34', first=True).find('span')
	    old_price = spans[0].text
	    discount = spans[1].text
	    print('Product Name: ', title)
	    print('New Price: ', price)
	    print('Old Price: ', old_price)
	    print('Discount: ', discount)
	    print()
	    csv_writer.writerow([title, price, old_price, discount])


	file.close()








