"""
File: web_crawler_avg.py
Name: Athena
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Get to know the average score of 250 movies
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('span', {'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})
	total = 0
	for tag in tags:
		score = float(tag['aria-label'][13:16])
		total += score
	print(total/25)



if __name__ == '__main__':
	main()
