# Reference Link: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
# Reference Link: https://realpython.com/python-requests/

import sys # Importing system module for dealing with command line arguments. 
argumensts = sys.argv # Getting the arguments list.

def help_():
    '''
        Purpose: help the user and show how to use the script.
        Parms: None
        Returns: None
    '''
    print(' - HELP:')
    print('\tScriptName.exe -d Playlist_LINK')
    sys.exit(0)

try:
    arg = sys.argv[1]
except IndexError as error:
    arg = '-h'    

if arg == '-h' or arg == '-help':
    help_()
elif arg == '-d' or arg == '-download':
    try:
        Playlist_LINK = argumensts[2].strip('\'')
    except IndexError as error:
        print('\nInvalid Arguments Supplied !\n')
        help_()
else:
    help_()    



# Import Required Libraries.
from requests_html import HTMLSession

# Importing Yourube_dl library to deal with youtube videos
import youtube_dl

def download(vformat,videoURL):
    '''
        Purpose: Download the Video in the specified format with in current directory
        Parms: 
            - vformat  # video format e.g: mp3 | mp4 | 1080p | 720p and so on...
            - videoURL # video URL e.g: https://www.youtube.com/watch?v=UbzwC15MXEA
        Returns: None
    '''
    ydl_parms = {'format':mformat}
    with youtube_dl.YoutubeDL(ydl_parms) as ydl: 
        ydl.download([videoURL])


# After Loading All The Libraries Stuff Take Input From User.

height = input('In which quality you want to download(1080 | 720 | 480 | 360 | 240 | best) ? ') # best with automatically dicide the best quality at runtime

if height == '1080' or height == '720' or height == '480' or height == '360' or height == '240' or height == 'best':
    print('Valid: ',height)
else:
    print('Input Not Valid')
    sys.exit(0) # Terminate the script if the arguments are not Valid.  

# Make the Format Playload Specified by the User.
mformat = f'best[height={height}]' if height == '1080' or height == '720' or height == '480' or height == '360' or height == '240' else height

# Search Barrier.
start = input('Do You Want to Start Search (y/n)? ')
if start != 'y':
    print('Emergency EXIT!')
    sys.exit(0) # Terminate the Script if user didnot want to continue... 

print('Searching...')
# Creating HTML Session
session = HTMLSession()

site_url = Playlist_LINK  # Youtube Playlist Link 

# Getting Response From the Site...
response = session.get(site_url)

html = response.html  # Taking HTML response of that request
html.render()

element_id = '#items' # select item having id = items
itemsList = html.find(element_id, first=True) # select single item

link_loc = 'a#wc-endpoint' # anchor having id = wc-endpoint
links = itemsList.find(link_loc) # find all items

meta_div = 'div#meta' # div with id = meta
meta_divs = itemsList.find(meta_div)

title_span = 'span#video-title' # Span having id = video-title
vid_titles = [x.find(title_span,first=True).text for x in meta_divs] # find all video titles.  

print('\n')  # Make Two Line Gap
print('Found Videos: ', len(vid_titles)) # Displays: How many videos has been found. 
print('-'*40) # Make a seperation
# Print all the Titles Found in [Playlist]
for title in vid_titles:
    print(title) 

print('-'*40) # Make a seperation

# Download Barrier.
start = input('\nDo You Want to Start Download (y/n)? ')
if start != 'y':
    print('Emergency EXIT!')
    sys.exit(0) # Terminates the script If the user Don't want to Donload the Files or Mode Changed.   

base_link = 'https://www.youtube.com' # Make a Base Link in order to concatinate withe the video id

start_index = 0 # Index-Pointer used to point the video link one by one.
while start_index != len(links): # Keep Doing it until it reaches total number of links Found 
    video_id, _, _ = links[start_index].attrs['href'].split('&')
    v_link = base_link + video_id
    try:
        print('') # Make a Line Gap
        print(f'{start_index}. -Video Title:{vid_titles[start_index]} -Downloading...') # Displays: - Link Index to Download and - Video Title  
        download(vformat=mformat,videoURL=v_link) # Download the Video
        start_index = start_index + 1 # Increment It, After it Successfully Download Video
    except Exception as error:
        print('Some Error Has Occured! Retrying Downloading... ') # Displays the Error Message.
    print('-'*40) # Make a seperation
