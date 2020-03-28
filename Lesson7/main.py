import json
from urllib.request import urlopen


# Reading JSON
with open("people.json", "r") as file:
    people = json.load(file)

for p in people:
    print(p["first_name"], "", p["last_name"])


# Using API
api_key = "b630ea59fceb766e46e360fa7ecf6806"
api = "http://api.openweathermap.org/data/2.5/weather?q=Ljubljana&units=metric&appid="

response1 = urlopen(api + api_key)
response2 = urlopen(api + api_key).read()

print("Response 1: ", type(response1))
print("Response 2: ", type(response2))


data1 = json.load(response1)
data2 = json.loads(response2)

print("Data 1: ", type(data1), data1)
print("Data 2: ", type(data2), data2)
print("\n----------------------\n")
print(data1["name"], data1["weather"][0]["description"])
