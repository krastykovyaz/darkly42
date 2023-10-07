#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from time import sleep

page = 'http://192.168.56.101/.hidden/'

def walking_over_dirs(url):
    uniq = set()
    count = 0
    def folder_scan(url):
        nonlocal count
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            link = a['href']
            if link[:2] == '..':
                continue
            elif link[-1] == '/':
                folder_scan(url + link)
            else:
                count += 1
                print(f'\rscanning item #{count}', end='')
                req2 = requests.get(url + link)
                if count % 10 == 0:
                    sleep(1)
                if req2.text not in uniq:
                    uniq.add(req2.text)
                    print('\n', req2.text, url + link)
    folder_scan(url)
    return count



if __name__ == '__main__':
    print(f'There are {walking_over_dirs(page)} items')
