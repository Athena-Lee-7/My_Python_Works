import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top/'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('div', {'class': 'sc-b189961a-7 feoqjK cli-title-metadata'})

	d = {}

	for tag in tags:
		year = tag.text[:4]
		if year not in d:
			d[year] = 1
		else:
			d[year] += 1
	for year, count in sorted(d.items(), key=lambda ele: ele[1]):
		print(year, '->', count)



if __name__ == '__main__':
	main()
