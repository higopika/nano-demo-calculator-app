import requests
import sys

url = "http://127.0.0.1:5000/calculator/add"
numbers = {"first": sys.argv[1], "second":sys.argv[2]}

response = requests.post(url, json = numbers)
print(response.status_code)
print(response.content)
