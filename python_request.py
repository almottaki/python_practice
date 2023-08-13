import requests
import json
r = requests.get('https://dummyjson.com/products')
products_data = r.json()
data = products_data['products']
for x in data:
    thisproduct = {
        "model": x["title"],
        "price": x["price"],
        "rating": x["rating"],
        "category": x["category"],

    }
    if x["price"] > 500 and x["rating"] > 4.50 and x["category"] == "smartphones":
        print(thisproduct)
    else:
        None

