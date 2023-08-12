             #url shortener source code in python

import requests
import sys


# A sample python code to shorten a URL with the use of cutt.ly APIs with different options.
class URLHandler:


    def __init__(self):
        self.api_key = None
        self.shortened_url = None
        self.exception_encountered = None


    def set_api_url(self):
        print("enter the api key of the service account::")
        input_api_key = input()
        self.api_url = input_api_key


    def get_input_url(self):
        print("Enter the URL that you want to shorten.")
        url_to_shorten = input()
        return url_to_shorten


        api_url = f"https://cutt.ly/api/api.php?key={self.api_key}&short={url}"
        request_return_obj = requests.get(self.api_url).json()["url"]

        try:
            if request_return_obj["status"] == 7:
                self.shortened_url = request_return_obj["shortLink"]
            else:
                self.shortened_url = None
        except Exception as e:
            self.exception_encountered = e


    def print_shortened_url(self):

        if self.shortened_url:
            print("Shortened URL: {}".format(self.shortened_url))
        else:
            print("URL shortening got an exception {}.".format(self.exception_encountered))



def main():
    shortner = URLHandler()
    url = None
    while (True):
        print("Please choose any one of the operations from the listed below the list of operations::")
        print("1. To enter the API key for the service account.")
        print("2. To enter the URL which you want to shorten.")
        print("3. To perform the operation of shortening the URL.")
        print("4. To print the URL which is shortened.")
        print("5. To exit from the code execution.")

        menu_choice = input()
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            shortner.set_api_url()
        elif menu_choice == 2:
            url = shortner.get_input_url()
        elif menu_choice == 3:
            # shortner.shorten_url(url)
            print("URL shortned successfully.")
        elif menu_choice == 4:
            shortner.print_shortened_url()
        elif menu_choice == 5:
            sys.exit()

        print("To keep on going with code execution, type [y] otherwise [n].")
        continue_or_exit = input()

        if continue_or_exit == 'y' or continue_or_exit == 'Y':
            pass
        elif continue_or_exit == 'n' or continue_or_exit == 'N':
            sys.exit()


if __name__ == '__main__':
    main()
