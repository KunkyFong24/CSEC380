# Name: Zachary Jensen
# Date: 1/26/2023

# Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# The 3 inputs required
domain = input("Enter domain: ")
url = input("Enter URL: ")
depth = input("Enter depth: ")
depth = int(depth)

#opens the file
filename = 'links.txt'
f = open(filename, 'w')

#gets all the site from the sitelist
def getAllSites(d, linksList):
    newLinksList = []

    #goes through all websites on a depth part of a linkedlist
    for x in linksList:
        if(str(x)[0:4] == "http"):
            page = urlopen(x)
            # Opens the URL, reads it and closes it
            pageToRead = page.read()
            page.close()

            # reads the page and opens up a file to put links in
            findLinks = bs(pageToRead, 'html.parser')


            #gets all the links in the current link list
            for link in findLinks.findAll('a'):
                links = link.get('href')
                linksTrue = link.get('href') is not None
                if(linksTrue == True and links != ""):

                    #adds the https://domain to all links that go through just the /
                    if (links[0] == "/"):
                        links = "https://" + domain + links

                    #goes through other links
                    if (links != "#"):
                        f.write(links + "\n")

                    # gets rid of empty #s to the list
                    if (links[0] != "#"):
                        newLinksList.append(links)

    #makes a new list for iteration
    linksList = newLinksList

    #returns the list
    return linksList

#makes the first link list for the first site
linksList = ["https://" + url]

#sets currentDepth to 0 at the start
currentDepth = 0

#while loop that increases the current depth when a depth search is completed. Main loop
while currentDepth <= depth:
    linksList = getAllSites(currentDepth, linksList)
    currentDepth = currentDepth + 1