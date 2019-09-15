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

    # Condense the dataframe to make it more readable
    price_tracker = pd.DataFrame(dict_list, columns=['Title', 'Shipping', 'Price'])  # Write the list of dictionaries]
    price_tracker = price_tracker.head(50)
    price_tracker['Title'] = price_tracker['Title'].str[12:30]  # Get the first 10 chars of the product
    price_tracker = price_tracker.astype(str)  # Convert everything to string
    return price_tracker


def save_plot(table_to_be_plotted):
    cell_text = []
    for row in range(len(table)):
        cell_text.append(table.iloc[row])
    plt.table(cellText=cell_text, colLabels=table.columns, loc='center')
    plt.axis('off')
    plt.savefig('price-table.pdf', bbox_inches='tight')


table = price_tracker_df(my_url)  # Cleaned up data for plotting
save_plot(table)  # Save the plots
