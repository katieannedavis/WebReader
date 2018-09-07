from bs4 import BeautifulSoup
import traceback
import requests
import logging
from gtts import gTTS


class UrlOpener:
    def __init__(self):
        self.logging_def()
        website = input("What is the url address?")
        page = self.open_address(website)
        html = self.parse_page(page)
        paragraph_box = html.find_all('p')
        self.read_words(paragraph_box)


    def open_address(self, address):
        """
        Requests opens page and retrieves data
        :param address: the web address
        :return: page - the response data
        """
        page = " "
        try:
            data = requests.get(address)
            page = data.text

        except requests.HTTPError:
            error = traceback.format_exc(limit=1)
            logging.warning(address + " produced an error " + error)
            print(error)

        return page

    def logging_def(self):
        """
        Starts event logging module.  The file Event_Log.log is opened, if it doesn't exist it will be created.
        Events will be logged by date then time followed by whatever event is given.
        :return: None
        """
        logging.basicConfig(filename='Event_Log.log', level=logging.WARNING,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


    def parse_page(self, content):
        """
        Translate request data into raw html.
        :param content:
        :return: html - the page's mark up
        """
        html = BeautifulSoup(content, 'html.parser')
        return html

    def read_words(self, p_tags):
        """
        Takes parsed array, starts appropriate speech engine, and feeds through array line by line
        :param p_tags: paragraph array
        :return:
        """
        text_to_read = ""
        for text in p_tags:
            text_to_read += text.text.strip()
        tts = gTTS(text=text_to_read, lang='en')
        file_name = input("What would you like to name your mp3 file? ")
        print("Please wait for completion of mp3 save. Times vary based on document size.")
        tts.save(file_name + ".mp3")
        print("Sound file saved as "+file_name+".mp3.")

UrlOpener()

