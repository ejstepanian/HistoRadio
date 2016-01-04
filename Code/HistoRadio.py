from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robobrowser import RoboBrowser
from random import randint

year = input('What year... would you like to HEAR?')
urlReal = "http://billboardtop100of.com/" + year + "-2/"

#This function creates a search using the input url

def songPick(url):
    browser = RoboBrowser(history=True)
    browser.open(url)
    song = browser.select('td')
    count = 0
    songName = []
    artistName = []
    y = 2
    while y == 2:
        for p in song:
            p = p.text
            if count == 1:
                artistName.append(p)
            elif count == 2:
                songName.append(p)
            count += 1
            if count == 3:
                count = 0

        x = randint(0,99)
        search = artistName[x] + " " + songName[x]
        if len(search) > 1:
            y = 3
            return(search,artistName[x],songName[x])

#These are some values to use later on

search,artist,song = songPick(urlReal)
print(song + ' by ' + artist)

#This function will search the song title on Youtube and return the url to the search results

def searchYoutube(search):
    b = webdriver.Firefox()
    b.get('https://www.youtube.com/')
    searchBar = b.find_element_by_name('search_query')
    searchBar.send_keys(search)
    searchBar.send_keys(Keys.RETURN)
    current = b.current_url
    b.close()
    return(current)

#This function will find a link to follow

follow = searchYoutube(search)
def getLink(artist,song,url):
    q = webdriver.Firefox()
    q.get(url)
    link = q.find_element_by_partial_link_text(artist)
    link.click()
getLink(artist,song,follow)
