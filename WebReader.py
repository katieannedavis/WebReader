from bs4 import BeautifulSoup
import urllib3
import traceback
import datetime
import logging


class UrlOpener:
    def __init__(self):
        self.logging_def()
        self.address = input("What is the url address?")
        page = " "
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', self.address, headers={}, timeout=4.0, retries=10)
            status = response.status
            print(status)
            page = response.data

        except TypeError:
            error = traceback.format_exc(limit=1)
            logging.debug(self.address + " produced a type error " + error)
            print(error)

        except urllib3.exceptions.NewConnectionError:
            error = traceback.format_exc(limit=1)
            logging.debug(self.address + " produced a type error " + error)
            print(error)
            print(self.address + " not found.  Please check address")

        except urllib3.exceptions.DecodeError:
            error = traceback.format_exc(limit=1)
            logging.debug(self.address + " produced a type error " + error)
            print(error)

        html = self.parse_page(page)
        print(html)

    def logging_def(self):
        """
        Starts logging errors and info
        :return:
        """
        logging.basicConfig(filename='Error_Log.log', level=logging.DEBUG,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def log_error(self, error):
        """
        Logs errors in error_log.txt and prints to screen
        :param: error
        :return: None
        """
        now = datetime.datetime.now()
        log_file = open("error_log.txt", "a+")
        log_file.write(now.strftime("%m/%d/%Y %H:%M") + "  -  " + error)
        log_file.close()
        return None

    def parse_page(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup


UrlOpener()

