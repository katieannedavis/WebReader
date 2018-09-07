from bs4 import BeautifulSoup
import traceback
import requests
import logging


class UrlOpener:
    def __init__(self):
        self.logging_def()
        website = input("What is the url address?")
        page = self.open_address(website)
        logging.info("Website data retrieved.")
        html = self.parse_page(page)
        logging.info("website html parsed")
        print(html)

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

        except requests:
            error = traceback.format_exc(limit=1)
            logging.debug(address + " produced an error " + error)
            print(error)

        return page

    def logging_def(self):
        """
        Starts event logging module.  The file Event_Log.log is opened, if it doesn't exist it will be created.
        Events will be logged by date then time followed by whatever event is given.
        :return:
        """
        logging.basicConfig(filename='Event_Log.log', level=logging.DEBUG,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


    def parse_page(self, content):
        """
        Translate urllib material into raw html.
        :param content:
        :return: html - the page's mark up
        """
        html = BeautifulSoup(content, 'html.parser')
        return html


UrlOpener()

