#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

page='http://192.168.56.101/?page=feedback'

def get_feedback(page,idx):
	req = requests.post(page, data = {
		'txtName':'',
		'mtxtMessage': chr(idx),
		'btnSign': 'Sign Guestbook'
		})
	soup = BeautifulSoup(req.text, 'html.parser')
	subj = soup.find('form').find_next_sibling()
	if subj.name != 'table':
		return "%03d %02x %c" % (idx, idx, chr(idx))

if __name__=='__main__':
	for idx in range(256):
		res = get_feedback(page,idx)
		if res is not None:
			print(res)
