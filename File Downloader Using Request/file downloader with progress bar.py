# Image URL for Downloading TEST
image='https://cdn.somethinghaute.com/wp-content/uploads/2019/08/FotoJet-24-1.jpg'
# MP3 URL for Downloading TEST 
mp3='https://www.macaronisoup.com/songs/mp3/TheWind.mp3'

# Importing Progress Bar Library
from tqdm import tqdm  
# Importing Os and Requests Modules 
import os,requests
def download(url):
    '''
        Purpose: Download the File with stream with chunk size = 1024
        Parms: url (Unified Resource Locator) represent unique file over INTERNET
        For User Experience It will show progress Bar :)
    '''
    response = requests.get(url,stream=True)  # Requesting the Stream Response
    total_size = int(response.headers['Content-Length'])  # Getting the Size of the File
    pbar = tqdm(total=total_size)  # Initilizing the Progress Bar with the file size
    file_name  = url.split("/")[-1]  # Split the URL to get the File Name
    with open(file_name, 'wb') as f:  
        for chunk in response.iter_content(chunk_size=1024): # Download 1024 bytes at single time means 1KB
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)   
                pbar.update(len(chunk))  # Update the Progress Bar
    pbar.close() # Close the Progress bar.  


def main():
    # For Demo purpose
    download(image)
    download(mp3)

if __name__ == '__main__':
    main()
