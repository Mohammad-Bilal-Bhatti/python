# Import Required Libraries.
from requests_html import HTMLSession

# Creating HTML Session
session = HTMLSession()
#--------------------------------------------
#      Basic Tabluar page to CRAWL
# -------------------------------------------
site_url = 'http://exam.muet.edu.pk/images'		# Site URL where directory access is not blocked
# -------------------------------------------

# Directory Name Where the Date will be stored or downloaded
save_dir = site_url[site_url.rfind('/')+1:]		# This will generally be the word ending after '/' from left side

# Printing on console that work is being started...
print('Collecting Data From : ',site_url)

# Getting Response From the Site...
response = session.get(site_url)

html = response.html 					# Taking HTML response of that request
selector = 'table'					# Basic selector element is table
table = html.find(selector,first=True)			# Find the first table in the HTML
titleRow = table.find('tr',first=True)			# Get the first Row for the Table, TitleRow, every time

header = []						# Making the header an empty list

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
		parms: 
			html_element:	Any HTML Elements List[] E.g: H1, P, IMG, A and so on...

		return: html_text[] : (of list type)
	"""
    e_list = []		# element list
    for element in html_element:
        e_list.append(element.text)
    return e_list

def downloadFile(link, file_name, dir_name):
	"""
		Purpose: To Download and Save the file in the specified directory, with the specified name, from the speicfied link.

		parms:
			~ link: 			http or https address
			~ file_name:			string
			~ dir_name:			string

		returns:	NONE

	"""
    print('-'*40)		# Make a line on console of easy reading...
    
    # Write the link form where the file is being downloading and where it is being saved
    print(f'Downloading:\nlink = {link} \nfile_name =  {file_name} \ndir_name = {dir_name}')
    
    import os			# Imporing Os module for acdessing file system.
	
    # Check the directory with specified name exists or not, 
    # if it doesnot exists make the directory with the that NAME
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
    try:
        new_session = HTMLSession()					# Create a new HTML Session
        res = new_session.get(link)					# Request the page and wait for the response.
        relative_path = dir_name + '/' + file_name
        if res.status_code == 200:					# If the status Code is [200] means [OK]
            content = res.content					# get is content
            file = open(relative_path,'wb')				# open a file in write mode
            file.write(content)						# write its content
            file.close()						# Close the file
        else:
        	print('File could not being Downloaded Reason: Response CODE = {}'.format(res.status_code))
    except Exception as e:
        print('Exception in Downloading')
        print(e)


download_link_indx = 1		# Download Link is generally present on the index

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
    td = tr.find('td')						# get the Table Data Elements list
    if( len( td ) > 0 ):					# if it founds it then:
        anchor = td[download_link_indx].find('a',first=True)	# Get the first anchor TAG in TD
        d_link = anchor.attrs['href']        			# Access the href property attribute.
        full_link = site_url + '/' + d_link
        #print(full_link)
        td = convertToTextEqui(td)				# Convert the TD ELEMENT LIST TO TEXT EQUIVALENT LIST
        # print(d_link)
        name = td[download_link_indx]				# Extract the name of the file
        name = name.lower()					# Lower case the name
        if(name != 'parent directory'):				# name CHECK just for proper Download
            downloadFile(full_link, d_link, save_dir)		# Call the Download Function and It will Download the file
        # print(name)
        #print(td)
        csv_writer.writerow(td)					# Write Date to the CSV File

file.close()	# Close the file when all done...

print('SUCCESS!!!')	# Print the success messeage to console.






