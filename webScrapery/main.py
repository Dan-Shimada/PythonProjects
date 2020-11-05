from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for items in links:
    item_text = items.find("a").text
    item_href = items.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        children = items.find("h2")
        print("Next simbling of the h2:", children.next_sibling)
