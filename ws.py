import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt

my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=80&PageSize=96'


def price_tracker_df(url_to_track):
    source = requests.get(url_to_track).text  # Get the complete text from the URL
    soup = bs(source, "html.parser").body  # Parse the HTML using Beautiful Soup
    dict_list = []  # List of all items and attributes i.e. list of dictionaries
    all_items = soup.find_all('div', class_='item-info')  # Find all divs of class "item-info"

    for item in all_items:
        row_dict = {}  # Initialise dictionary
        title = str(item.find_all('a', class_='item-title')[0].text).replace("\r\n ", "")
        price = str(item.find_all('li', class_='price-current')[0].strong.text).replace("\r\n ", "")
        shipping = str(item.find_all('li', class_="price-ship")[0].text).replace("\r\n ", "")
        row = (('Title', title), ('Shipping', shipping.strip()), ('Price', price.replace(",", "")))
        row_dict.update(row)  # New dictionary updated onto the old one
        dict_list.append(row_dict)  # Append the new dictionary to the list of dictionaries
    price_tracker = pd.DataFrame(dict_list, columns=['Title', 'Shipping', 'Price'])  # Write the list of dictionaries
    # to a pandas dataframe

    return price_tracker['Price'].astype(str).astype(int)


price_tracker = price_tracker_df(my_url)
plt.plot(price_tracker)
plt.xlabel('Title')
plt.ylabel('Price')
plt.show()
# price_tracker.plot.bar(x='Title', y='Price')
