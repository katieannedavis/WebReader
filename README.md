# Py-Webby
--------------------------------------------------
Py-Webby will convert a web page to a mp3 file. This program features Python 3's BeautifulSoup, requests, and gtts (Google text to speech) libraries.  It uses requests to web scrape the data from a desired webpage.  It then sends that data through BeautifulSoup to find all paragraph text.  Finally, that text is arranged in a string and fed into gtts which produces the mp3 file.

## Required modules
* Requests (pip install requests)
* BeautifulSoup (pip install BeautifulSoup4)
* GTTS (pip install gTTS)
