# import requests
# import json
# r = requests.get('https://dummyjson.com/products')
# products_data = r.json()
# data = products_data['products']
# for x in data:
#     thisproduct = {
#         "model": x["title"],
#         "price": x["price"],
#         "rating": x["rating"],
#         "category": x["category"],
#
#     }
#     if x["price"] > 500 and x["rating"] > 4.50 and x["category"] == "smartphones":
#         print(thisproduct)



# import requests
# import json
# r = requests.get('https://dummyjson.com/carts')
# product = r.json()
# data = product['carts']
#
# for x in data:
#     print(x['products'])



# import requests
# r = requests.get('https://www.freecodecamp.org/news/content/images/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg')
#
# with open('python.jpg', 'wb') as f:
#     f.write(r.content)



# import requests
# r = requests.get('https://www.freecodecamp.org/news/content/images/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg')
#
# print(r.headers)


# import requests
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', 'payload')    #url=https://httpbin.org/get?page=2&count=25
# #print(r.text)
# print(r.url)


# import requests
# payload = {'username': 'mottaki', 'id': 1}
# r = requests.post('https://httpbin.org/post', data=payload)
# # print(r.text)
# print(r.json())