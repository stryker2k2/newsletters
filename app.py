import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
req_urls = [
    'https://futureparty.com/',
    'https://www.marketingbrew.com/',
    'https://buffer.com/',
    'https://www.milkkarten.net/',
    'https://geekout.mattnavarra.com/'
    ]


def find_type(soup):
    email_type = soup.find(type='email')
    if email_type:
        print('[+] Found \'email\' on webpage')
        # print(email_type.prettify()\n)
        regex = re.compile(r'placeholder')
        if regex.search(str(email_type)):
            print('[+] Webpage has a placeholder for user to input email')
            # print(email_type.prettify()\n)
        else:
            print('[!] Did not find a placeholder for user to input email')
    else:
        print('[!] Did not find \'email\' on webpage')


def main():
    print("** Newsletter Request Module **")
    for req_url in req_urls:
        req = requests.request("GET", req_url, headers=headers)
        if (req.status_code == 200):
            print(f'\n[+] {req_url}')
            print('[+] Status Code: 200')
            soup = BeautifulSoup(req.content, 'html.parser')
            find_type(soup)
        else:
            print(f'\n[+] {req_url}')
            print(f'[+] Status Code: {req.status_code}')


if __name__ == "__main__":
   main()