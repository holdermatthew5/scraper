import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Sonoluminescence'

def get_citations_needed_count(url):
    response = requests.get(url)
    parsed = BeautifulSoup(response.content, 'html.parser')
    p_tags = parsed.find_all('p')
    total = 0
    for i in range(len(p_tags)):
        if p_tags[i].find('sup', class_='noprint'):
            for i in p_tags[i].find_all('sup', class_='noprint'):
                total += 1
    return total

def get_citations_needed_report(url):
    response = requests.get(url)
    p_tags = BeautifulSoup(response.content, 'html.parser').find_all('p')
    passages = ''
    for i in range(len(p_tags)):
        if p_tags[i].find('sup', class_='noprint'):
            passages = f'{passages}\n{p_tags[i]}'
    return passages

if __name__ == '__main__':
    print('count:', get_citations_needed_count(url))
    print('report', get_citations_needed_report(url))