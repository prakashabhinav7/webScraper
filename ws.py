from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#TODO Create function for reader(to copy data from the url/list of urls)
#TODO Create function for writing results to file/db

my_url = 'https://www.newegg.com/Video-Cards-Devices/Category/ID-38'
uClient = uReq(my_url)  # opens connection
page_html = uClient.read()  # reads the page
uClient.close()  # disconnect client

page_soup = soup(page_html, "html.parser")  # html parsing

#TODO grab each product and test out the traversal for each product
containers = page_soup.find_all("ul", {"class": "item-features"})

#TODO implement try except for boundary cases
for container in containers:
    # brand = container.div.div.a.img["title"]
    print(container.li)

# print(container)
# f = open('deleteme.html', 'w')
# f.write(str(container))
# f.close()


# print(page_soup.h1)
# print(page_soup.body.span)
