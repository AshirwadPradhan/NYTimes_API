import requests
from bs4 import BeautifulSoup

URL = 'https://www.nytimes.com/'
nyt_text = []
nyt_link = []

def get_source():
    global URL
    try:
# getting the source code
        sc = requests.get(URL)
        if sc.status_code == 200:
            print('Retrieved Webpage')
            return sc.text
    except Exception:
        print('Cannot retrieve webpage {}'.format(URL))


def parse_source(number_of_links=20):
    sc = get_source()

# encoding the source
    sc = sc.encode('ascii', 'ignore')
    soup = BeautifulSoup(sc, 'html.parser')

# collecting all the news links
    a_links = soup.find_all('h2', {'class' : 'story-heading'})
    a_links = BeautifulSoup(str(a_links), 'html.parser')
    a_links = a_links.find_all('a')

    
# collecting top 10 links from a_links
    a_links_text = []
    for i,a_tags in enumerate(a_links):
        if i < number_of_links:
            a_links_text.append(a_tags.get_text())
        else:
            break


# collecting the links of top 10 news
    a_links_link = []
    for i,a_tags in enumerate(a_links):
        if i < number_of_links:
            a_links_link.append(a_tags['href'])
        else:
            break

    return (a_links_text, a_links_link)

nyt_text, nyt_link = parse_source()