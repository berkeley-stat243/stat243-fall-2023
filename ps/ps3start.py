import requests
from bs4 import BeautifulSoup

## Code to extract the URLs for the individual speeches.

master_url = "https://www.presidency.ucsb.edu/documents/presidential-documents-archive-guidebook/annual-messages-congress-the-state-the-union#axzz265cEKp1a"

content = requests.get(master_url).content
html = BeautifulSoup(content, 'html.parser')
elems = html.select("table a")
# using list comprehension
all_urls = [x.get('href') for x in elems]
# or using `map()`
all_urls = list(map(lambda x: x.get('href'), elems))

all_text = [x.get_text() for x in elems]

rg = list(map(str, range(1790, 2024)))
included = list(map(lambda x: x in rg, all_text))

speech_urls = [x for x, incl in zip(all_urls, included) if incl]
years = [int(x) for x, incl in zip(all_text, included) if incl]

sorted_speeches = sorted(zip(years, speech_urls))

## This syntax should work to get the text corresponding to the speech text.
## Shown here for one speech as an example.

url = "https://www.presidency.ucsb.edu/ws/index.php?pid=4117"
content = requests.get(url).content
html = BeautifulSoup(content, 'html.parser')
html.find("div", attrs = {'class': 'field-docs-content'}).get_text()
# Note that a good assertion would be to check that there is only
# one such `div` element.



