import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Max_Baer_(boxer)'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

citation = 'citation needed'

citations = soup.find_all(text=citation)


def get_citations_needed_count():
    print('The total number of citations needed is: ', len(citations))
    return len(citations)

def get_citations_needed_report():
    for text in citations:
        soup_text = text.find_parent('p')
        split_text = soup_text.text.split()
        print(' '.join(split_text))
        print(' ')


if __name__ == '__main__':
    get_citations_needed_count()
    get_citations_needed_report()
