import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

r = requests.get("https://www.tutorialspoint.com/index.htm")

soup = BeautifulSoup(r.content)

text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print(c.most_common())


print([x for x in c if c.get(x) > 5])  # words appearing more than 5 times
