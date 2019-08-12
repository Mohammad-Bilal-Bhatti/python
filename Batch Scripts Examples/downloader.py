# Import Required Libraries.
from requests_html import HTMLSession


# Download File Module
# Responsible for downloading the file.
def downloadFile(link, file_name, dir_name):
    """
    Purpose: To Download and Save the file in the specified directory, with the specified name, from the speicfied link.
    parms:
        ~ link:            http or https address
        ~ file_name:       string
        ~ dir_name:        string
        returns:        NONE
    """
    print('-'*40)        # Make a line on console of easy reading...
    # Write the link form where the file is being downloading and where it is being saved
    print(f'Downloading:\nlink = {link} \nfile_name =  {file_name} \ndir_name = {dir_name}')    
    import os       # Imporing Os module for acdessing file system.    
    # Check the directory with specified name exists or not, 
    # if it doesnot exists make the directory with the that NAME
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
    try:
        new_session = HTMLSession()                # Create a new HTML Session
        res = new_session.get(link)                # Request the page and wait for the response.
        relative_path = dir_name + '/' + file_name
        if res.status_code == 200:                 # If the status Code is [200] means [OK]
            content = res.content                  # get is content
            file = open(relative_path,'wb')	       # open a file in write mode
            file.write(content)	                   # write its content
            file.close()                           # Close the file
        else:
            print('File could not being Downloaded Reason: Response CODE = {}'.format(res.status_code))
    except Exception as e:
        print('Exception in Downloading')
        print(e)

# Creating HTML Session
session = HTMLSession()

site_url = 'https://www.robvanderwoude.com/batexamples.php'

# Make the root as the site url
root = site_url[:site_url.rfind('/')]

# Printing on console that work is being started...
print('Collecting Data From : ',site_url)

# Getting Response From the Site...
response = session.get(site_url)

# Getting the html of the page.
html = response.html

table_id = '#Examples'

table = html.find(table_id,first=True)

# find all the rows in the table.
t_rows = table.find('tr')

save_dir = 'downloads'

start_index = 2
for index in range(start_index,len(t_rows)):
    anchor_tag = t_rows[index].find('a',first=True)
    file_reference = anchor_tag.attrs['href']
    download_link = root + '/' + file_reference
    file_name = file_reference[file_reference.find('/')+1:]
    downloadFile(download_link,file_name,save_dir)






    

















