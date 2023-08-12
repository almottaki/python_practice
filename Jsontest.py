# json means (JavaSript Objest Notation)
# json format :
#            1.json array object (Array need for Multiple data)
#            2.formatted string
#            3.key value pair
#
# Why Json?
#    For Rest API






# import json
#
# x =  '{"name":"MOTTAKI", "age":"21", "home":"Rangpur"}'
#
# y = json.loads(x)
#
# print(y["age"])



# import json
#
# data = {
#     "MOTTAKI": [
#         {
#             "Age": "21",
#             "Date of Birth": "16-09-2002",
#             "Education": [
#             "JSC",
#             "SSC",
#             "DIPLOMA"
#             ]
#         }
# ],
#     "MARJIA": [
#         {
#             "Age": "15",
#             "Date of Birth": "13-12-2008",
#             "Education": [
#             "PSC",
#             ]
#         }
#
# ]
# }
#
# x = json.dumps(data)
# print(x["MARJIA"])


# import json
#
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "banana"]))
# print(json.dumps(("apple", "banana")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, sort_keys=True))


# import json
# file=open("/home/mottaki/Documents/sample.json", "r")
# x=file.read()
# print(json.loads(x))
# print(json.loads(x["Education"]))

# import json
#
# x = '{"name":"MOTTAKI", "age":"21", "home":"Rangpur"}'
#
# x['test'] = True
# print(json.dumps(x))

# import json
# file=open("/home/mottaki/Documents/sample.json", "w")
# x=file.write('{"name":"MOTTAKI", "age":"21"}')
# y = json.dumps(x)
# print(y)