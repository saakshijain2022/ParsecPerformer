import requests
from bs4 import BeautifulSoup

# result = requests.get("https://www.google.co.in/")
# print(result.text)

# print(result.status_code)
# lets us know whether the page is accessible or not
# output - 200 code if you get means content you wanted is extracted and response is ok

# print(result.headers)
# some other info

# src = result.content
# lets us store the page content of the website accessed from requests to a variable 
# print(src)

# request1=requests.get("https://www.amazon.in/Echo-Dot-3rd-Gen/dp/B07PFFMP9P/ref=sr_1_1?adgrpid=54712015810&ext_vrnc=hi&hvadid=398059830697&hvdev=c&hvlocphy=1007788&hvnetw=g&hvqmt=b&hvrand=4617156484205132033&hvtargid=kwd-358111533759&hydadcr=24570_1971435&keywords=echo%2Bdot%2Bbest&sr=8-1&th=1")
# request1.text

# soup = BeautifulSoup(src,"lxml")
# now we have the page source code stored, we will use Beautifl Soup module to parsec anf process the source

# links = soup.find_all("a")
# print(links)
# print("\n")

# for link in links:
#     if "About" in link.text:
#         print(link)
        # <a href="/intl/en/about.html">About Google</a>
        # print(link.attrs['href'])


# task 2

# goal- extract all of the links on the page that point to the briefings and statements

result = requests.get("https://www.whitehouse.gov/briefing-room/")
src= result.content
# print(src)
soup = BeautifulSoup(src,"lxml")

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs['href'])

print(urls)
