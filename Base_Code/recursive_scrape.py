
from subprocess import *
import os
import urllib2
from time import sleep

#to get all the pages just add append base_url/index(index).html
#for craigslist casual encounters this is  newyork.craigslist.org/cas/index100.html
#where the 1 in index100 will be incremented to get all pages.

urls_to_scrape = open("urls_to_scrape.txt","r")
current_dir = os.getcwd()
if not os.path.exists("results"):
    os.mkdir("results")

urls_to_pages = open("urls_to_pages.csv","a")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0
for url in urls_to_scrape:
    try:
        url_object = urllib2.urlopen(url)
    except urllib2.HTTPError:
        continue
    
    url_text = ''
    for i in url_object:
        url_text += i

    print "splitting the url for name creation.."
    seg_url = url.split("/")
    file_name = seg_url[-2]
    file_name = file_name+".html"
    scraper = "craigslist"+(seg_url[-1].split(".")[0])+"scraper"
    unique_url = alphabet[counter%52]+"_"+"craigslist"+(seg_url[-1].split(".")[0])
    
    print "moving link into results.."

    os.chdir("results")
    with open(unique_url,"w") as url_file:
        url_file.write(url_text)
    
    

    os.chdir("../")
    urls_to_pages.write(url+","+unique_url+"\n")


    counter += 1
    print counter
    

urls_to_pages.close()
