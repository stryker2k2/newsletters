import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
req_urls = [
    'https://managingeditor.substack.com/',
    'https://actionnetwork.org/forms/sign-up-for-political-social-grab-bag-email',
    'https://futureparty.com/',
    'https://www.marketingbrew.com/',
    'https://buffer.com/',
    'https://www.milkkarten.net/',
    'https://geekout.mattnavarra.com/',
    'https://www.axios.com/newsletters/axios-am',
    'https://www.aspeninstitute.org/ideas/',    
    'https://www.cnn.com/specials/newsletter--5-things',    
    'https://www.politico.com/playbook',
    'https://alearningaday.blog/',
    'https://example.com/'   # Demo of what 'No Newsletter' looks like
    ]


def find_type(req, soup):
    email_type = soup.find(type='email')
    if email_type:
        # print('[+] Found \'email\' on webpage')
        # print(email_type.prettify()\n)
        regex = re.compile(r'placeholder')
        if regex.search(str(email_type)):
            print(f'[+] {req.url}')
            # print(email_type.prettify())
        else:
            print(f'[!] {req.url} - No Newsletter (no placeholder)') # Does not have a placeholder
    else:
        print(f'[!] {req.url} - No Newsletter (no email type)') # Does not have <type="email"> on webpage


def main():
    print("** Newsletter Request Module **")
    for req_url in req_urls:
        req = requests.request("GET", req_url, headers=headers)
        if (req.status_code == 200):
            # print(f'\n[+] {req_url}')
            # print('[+] Status Code: 200')
            soup = BeautifulSoup(req.content, 'html.parser')
            find_type(req, soup)
        # else:
        #     print(f'\n[+] {req_url}')
        #     print(f'[+] Status Code: {req.status_code}')


if __name__ == "__main__":
   main()