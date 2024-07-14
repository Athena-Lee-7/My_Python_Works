import requests
from bs4 import BeautifulSoup

url2 = 'https://notify-api.line.me/api/notify'
token = 'UY15TlIrmfer8s9u78qHvA9kSkHfW3bwQOTFTCSjw1S'
headers = {
    'Authorization': 'Bearer ' + token
}

url = 'https://www.shopback.com.tw/all--stores'
r = requests.get(url)
r.encoding = r.apparent_encoding

sp = BeautifulSoup(r.text, 'html.parser')  

lines = sp.find_all(class_="atom__typo atom__typo--type-cashback")

s = []

for e in lines:
    text = e.text.strip()
    if '限時' in text:
        s.append(text)

logo_urls = []

logo_elements = sp.find_all(attrs={"data-merchant-name": True, "data-opportunity-type": "upsize"})

for element in logo_elements:
    logo_url = element.get("data-merchant-name")
    logo_urls.append(logo_url)

combined_info = [f'{merchant} {upsize}' for merchant, upsize in zip(logo_urls, s)]

message = '\n'.join(combined_info)

response = requests.post(url2, headers=headers, data={'message': '\n'+message})
print(response.text)
