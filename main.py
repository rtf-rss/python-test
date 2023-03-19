from bs4 import BeautifulSoup as bs
import requests

LINK = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=mobile+samsung&_sacat=0&LH_TitleDesc=0&_odkw=telephone+samsung&_osacat=0"

def get_prices_by_link(link):
#     get source
    r = requests.get(link)
#     parse source
    page_parse = bs(r.text, 'html.parser')
#     print(page_parse)
#     find all list items from search results
    search_results = page_parse.find("ul", {"class":"srp-results"}).find_all("li", {"class":"s-item"})
    
    item_prices = list()
#     price_as_text = ""
    
    for result in search_results:
        price_as_text = result.find("span", {"class":"s-item__price"}).text
        if "to" in price_as_text:
            continue
        price = float(price_as_text[1:].replace(",", ""))
        item_prices.append(price)
    print(len(item_prices))
    return item_prices



if __name__ == "__main__":
    print(get_prices_by_link(LINK))