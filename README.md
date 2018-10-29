# WebReader
--------------------------------------------------
WebReader will convert a web page to a mp3 file. This program features Python 3's BeautifulSoup, requests, and gtts (Google text to speech) libraries.  It uses requests to web scrape the text from a desired webpage.  It then sends that text through BeautifulSoup to find all paragraph text.  Finally, that text is arranged in a string and fed into gtts which produces the mp3 file.  This program will create a directory called "WebReaderMp3s" in your "Music" directory or if that's missing, then your "Documents".

This program can read multiple languages.  I have tested it in English, Spanish, and Korean.

## Required modules
* Requests (pip install requests)
* BeautifulSoup (pip install BeautifulSoup4)
* GTTS (pip install gTTS)

## Packaging
Pyinstaller was used to make an executable of this file.  The icon.ico has the multilayers needed for pyinstaller to make an icon that expands if the user chooses to have their icons a differ size.
The command used to package this was: 
* pyinstaller -F --icon="icon.ico" WebReader.py

-F means one file
