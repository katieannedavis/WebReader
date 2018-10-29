from bs4 import BeautifulSoup
import urllib.request
import gtts
from pathlib import Path
import os


class UrlOpener:
    def __init__(self, website, new_file):
        self.website = website
        self.new_file = new_file
        if website[0:8] == "https://" or website[0:7] == "http://":
            page = self.open_address(website)
            html = self.parse_page(page)
            paragraph_box = html.find_all('p')
            mp3folder = self.make_dir()
            self.read_words(paragraph_box, mp3folder, new_file)
        else:
            paragraph_box = 'The address '+website+' was an invalid web address. ' \
                                                   'Please begin address with either https colon slash slash or' \
                                                   ' http colon slash slash'
            mp3folder = self.make_dir()
            self.error_message(paragraph_box, mp3folder, new_file)

    def make_dir(self):
        """
        Creates Mp3 directory if none exists.  Program will try to put folder in Music,
        but failing that it will put the mp3 folder in Documents.
        :return: sound_dir - the folder location
        """
        music_path = Path.home().joinpath('Music')
        working_dir = 'WebReaderMp3s'
        try:
            os.mkdir(music_path.joinpath(working_dir))
            sound_dir = music_path.joinpath(working_dir)

        except FileNotFoundError:
            music_path = Path.home().joinpath('Documents')
            sound_dir = music_path.joinpath(working_dir)

        except FileExistsError:
            sound_dir = music_path.joinpath(working_dir)

        print("Your mp3 will be created in " + str(sound_dir))
        return sound_dir

    def open_address(self, address):
        """
        Requests opens page and retrieves data
        :param address: the web address
        :return: page - the response data
        """

        try:
            page = urllib.request.urlopen(address).read()

        except:
            page = "Can't retrieve web address. Please check the address and try again."

        return page

    def parse_page(self, content):
        """
        Translate request data into raw html.
        :param content:
        :return: html - the page's mark up
        """
        html = BeautifulSoup(content, 'html.parser')
        return html

    def read_words(self, p_tags, folder, file_name):
        """
        Takes parsed array, starts appropriate speech engine, and feeds through array line by line
        :param p_tags: paragraph array
        :param folder: folder where mp3s are created and played from
        :param file_name: what the mp3 is named
        :return:
        """
        text_to_read = ""
        for text in p_tags:
            text_to_read += text.text.strip()
        if text_to_read == "":
            text_to_read = 'Website retrieval failed. Please check address and try again.'
        try:
            tts = gtts.gTTS(text=text_to_read, lang='en')
            print("Please wait for completion of mp3 save. Times vary based on document size.")
            tts.save(folder.joinpath(file_name + ".mp3"))
            sound_file = folder.joinpath(file_name + ".mp3")
            message = sound_file
            print(message)
            return message
        finally:
            pass

    def error_message(self, message, folder, file):
        try:
            tts = gtts.gTTS(text=message, lang='en')
            print("Error in web address. Mp3 is audio error alert.")
            tts.save(folder.joinpath(file + ".mp3"))
            sound_file = folder.joinpath(file + ".mp3")
            message = sound_file
            print(message)
            return message
        finally:
            pass


def main():
    print('Welcome to WebReader')
    print('--------------------')
    end = "2"
    while end != "9":
        http_address = input('What is the web address you would like to convert? (Please include the full address.)')
        if http_address != "":
            mp3_name = input('What would you like to name your audio track?')
            if mp3_name == "":
                print('Please enter a name for your mp3.')
            else:
                try:
                    UrlOpener(http_address, mp3_name)
                except gtts.tts.gTTSError:
                    print('Translator could not understand this website. It may have created a partial file named '
                          + mp3_name + ".mp3")
                    pass
        else:
            print('Please enter a web address or exit.')
        end = input('Press 1 to create another mp3, or press 9 to exit')


if __name__ == '__main__':
    main()
