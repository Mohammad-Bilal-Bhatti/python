# Image URL for Downloading TEST
image='https://cdn.somethinghaute.com/wp-content/uploads/2019/08/FotoJet-24-1.jpg'
# MP3 URL for Downloading TEST 
mp3='https://www.macaronisoup.com/songs/mp3/TheWind.mp3'

# Importing Os and Requests Modules 
import os,requests
# Importing Time Module
import time

def download(url):
	'''
	'''
    start_time = time.time() # Noting Down the start time 
    get_response = requests.get(url,stream=True)  # Requesting the Stream Response
    file_name  = url.split("/")[-1]  # Split the URL to get the File Name
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):  # Download 1024 bytes at single time means 1KB
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    end_time = time.time()  # Noting Down the end time 
    print(f'Time Required To Download File {file_name}: {(end_time-start_time)}')  # Printing the escaped in downloading the file 

def main():
    # For Demo purpose
    download(image)
    download(mp3)

if __name__ == '__main__':
    main()    