# Import Required Libraries.
from requests_html import HTMLSession

# Creating HTML Session
session = HTMLSession()
#--------------------------------------------
#      Basic Tabluar page to CRAWL
# -------------------------------------------
site_url = 'http://exam.muet.edu.pk/images'		# Site URL where directory access is not block
# -------------------------------------------

# Directory Name Where the Date will be stored or downloaded
save_dir = site_url[site_url.rfind('/')+1:]		# This will generally be the word ending after '/' from left side

# Printing on console that work is being started...
print('Collecting Data From : ',site_url)

# Getting Response From the Site...
response = session.get(site_url)

html = response.html 	# Taking HTML response of that request

selector = 'table'		# Basic selector element is table

table = html.find(selector,first=True)	# Find the first table in the HTML

titleRow = table.find('tr',first=True)	# Get the first Row for the Table, TitleRow, every time

header = []		# Making the header an empty list

# For each table-header element in titleRow, find the text in it, and append to the list...
for tableHead in titleRow.find('th'):	
    #print(tableHead.text)
    header.append(tableHead.text)

# Importing CSV module for Writing Date to File
import csv
name = site_url[site_url.rfind('/')+1:]		# name of the file would be same as name of directory described above.
file_name = name + '.csv'
file = open(file_name, 'w')
csv_writer = csv.writer(file)
csv_writer.writerow(header)

def convertToTextEqui(html_element):
	"""
		Purpose: To convert html_element list into html_text equivelent
		parms: html_element		Any HTML Element E.g: H1, P, IMG, A and so on...

		return: html_text
	"""
    e_list = []		# element list
    for element in html_element:
        e_list.append(element.text)
    return e_list

def downloadFile(link, file_name, dir_name):
	"""
		Purpose: To Download and Save the file in the specified directory, with the specified name, from the speicfied link.

		parms:
			~ link 			http or https address
			~ file_name		string
			~ dir_name		string

		returns:	NONE

	"""
    print('-'*40)
    print(f'Downloading:\nlink = {link} \nfile_name =  {file_name} \ndir_name = {dir_name}')
    import os
    # Check the directory with specified name exists or not, 
    # if it doesnot exists make the directory with the that NAME
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
    try:
        new_session = HTMLSession()
        res = new_session.get(link)
        relative_path = dir_name + '/' + file_name
        if res.status_code == 200:
            content = res.content
            file = open(relative_path,'wb')
            file.write(content)
            file.close()
    except Exception as e:
        print('Exception in Downloading')
        print(e)


download_link_indx = 1

# ---------------------------------------------------
# TODO:
# Scenario: link can lead to other site structure...
# ---------------------------------------------------
# ---------------------------------------------------

skipFirst = True
# For each tr in table skip the first header...
for tr in table.find('tr'):
    if skipFirst == True:
        skipFirst = False;
        continue
    td = tr.find('td')
    if( len( td ) > 0 ):
        anchor = td[download_link_indx].find('a',first=True)
        d_link = anchor.attrs['href']        
        full_link = site_url + '/' + d_link
        #print(full_link)
        td = convertToTextEqui(td)
        # print(d_link)
        name = td[download_link_indx]
        name = name.lower()
        if(name != 'parent directory'):
            downloadFile(full_link, d_link, save_dir)
        # print(name)
        #print(td)
        csv_writer.writerow(td)	# Write Date to the CSV File

file.close()

print('SUCCESS!!!')






