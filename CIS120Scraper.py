import sys
import os, urllib, re
from bs4 import BeautifulSoup

#working directory must be C:\Users\Brent\Documents\CIS 120


global local_path

#opens class web page, reads it, and implements BeautifulSoup
url = urllib.urlopen("http://www.seas.upenn.edu/~cis120/current/lectures.shtml")
page = url.read()
parsed = BeautifulSoup(page)

#finds all links in page
links = parsed.find_all('a', href=True)

for link in links:

    if "lectures/" in str(link):
        href = link['href']
        
        #gets last expression in link
        file = re.findall('[^\/]+$', href)
        file = file[0]
        
        if "/lec" in str(href):
            
            #local directory for my files
            #changes necessary for use on other computer
            base_path = "C:\Users\Brent\Documents\CIS 120\Lectures"
            
            file_name = file.replace(".pdf", "")
            local_path = os.path.join(base_path, file_name)
            
            #create folder for files if not already created
            if not os.path.exists(local_path): os.makedirs(local_path)
        
        head = "http://www.seas.upenn.edu/~cis120/current/"
            
        #downloads and saves files to chosen directory
        f = open(str(os.path.join(local_path, file)), 'wb')
        f.write(urllib.urlopen(os.path.join(head,href)).read())
        f.close