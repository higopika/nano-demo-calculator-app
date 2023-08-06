import sys
import requests
import types
from requests.exceptions import ConnectionError

if len(sys.argv) != 3:
    print("usage : post_add.py <num1> <num2>")
    print("result is a dictionary {\"result\":<Value>}")
    exit(1)

'''
print(isnumeric(sys.argv[1]))
print(isinstance(sys.argv[1],int))
print(isinstance(sys.argv[1],int) == True)

if (isinstance(sys.argv[1],int) != True) or (isinstance(sys.argv[2],int) != True):
    print("Integers should be provided. Cannot add non integers")
    exit(1)

'''

url = "http://127.0.0.1:5000/calculator/add"
print(sys.argv)

numbers = {"first": sys.argv[1], "second" : sys.argv[2]}
response = None

try:
    response = requests.post(url,json = numbers)
except ConnectionError as e:
    print("Could not connect to server")
except:
    print("Something occured")


print(response.status_code)
print(response.content)
