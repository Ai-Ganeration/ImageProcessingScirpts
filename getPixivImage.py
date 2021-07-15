from bs4 import BeautifulSoup
import validators
import requests
import re

IMAGE_SOURCE_SITE = "https://www.pixiv.net/ranking.php?mode=daily"

responsePage = requests.get(IMAGE_SOURCE_SITE)
responseSoup = BeautifulSoup(responsePage.content, "html.parser")

# hardcoded id for #1 ranked image
responseElement = responseSoup.find(id=1)
responseSet = responseElement.find_all("a", class_="title")
responseTag = responseSet[0]
responseURL = responseTag["href"]

RankedFirstURL = "https://www.pixiv.net/en" + responseURL
assert(validators.url(RankedFirstURL) == True)

# find the numerical id
image_id = re.search(r'.*/(\d*)', RankedFirstURL).group(1)

# get source for image
imagePage = requests.get(RankedFirstURL)
imageSoup = BeautifulSoup(imagePage.content, "html.parser")

# find the image url
sourceURL = re.findall(r'https://i.pximg.net/img-original/img/.*?'+image_id+'.*?.png', str(imageSoup))

headers_dict = {"Referer": "https://www.pixiv.net/"} # for accessing image
with open('image.png', 'wb') as f:
    for s in sourceURL:
        f.write(requests.get(s, headers=headers_dict).content)
