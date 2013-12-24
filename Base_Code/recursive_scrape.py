
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
# for url in urls_to_scrape:
    
    # print "splitting the url for name creation.."
    # seg_url = url.split("/")
    # file_name = seg_url[-2]
    # file_name = file_name+".html"
    # scraper = "craigslist"+(seg_url[-1].split(".")[0])+"scraper"
    # unique_url = alphabet[counter%52]+"_"+"craigslist"+(seg_url[-1].split(".")[0])
    
    # print "moving into the newly created unique directory for scraping.."
    # os.mkdir(unique_url)

    
#     print "copying scraper generation files..."
#     call(['cp','./recursive_generate.py', unique_url+'/recursive_generate.py'])
#     call(['cp','./hash_scrap.py', unique_url+'/hash_scrap.py'])
#     os.chdir(unique_url)
#     config = open("config.txt","w")
#     config.write(url)
#     config.close()
#     print os.getcwd() 

# # this is necessary because of the way the process works.  Making a call to OS allows all other processes to finish.  Without a print os.getcwd() or some call to OS, this code does not work.

#     print "scraping..."
#     call(['python','recursive_generate.py'])
#     call(['python','hash_scrap.py'])
    
#     print os.getcwd() #ensures call processes finish
    
#     print "moving results into results folder.."
#     os.chdir(scraper)
#     unique_file_name = unique_url+".html"
    
#     print os.getcwd() #just being careful
#     call(["mv", "./"+file_name, "./"+unique_file_name])
#     call(["cp", unique_file_name, "../../../results/"+unique_file_name])
#     print os.getcwd()
    
#     counter += 1
#     os.chdir(top_level)
    

# For all links in urls_to_scrape we will need to create a directory with that link's name, copy/paste in generate.py and hash_scrap.py. Then we will need to run generate.py and hash_scrap.py, move the results up to the top level of the directory structure.  Finally, we'll need to merge all the data into a database.  For this reason, it makes sense for the data to be in .txt or .csv format so that it can be read like a normal file.

