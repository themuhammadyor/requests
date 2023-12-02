import httpx
import os
from pprint import pprint
import json
# url ='https://jsonplaceholder.typicode.com/todos'
# response = httpx.get(url=url)
# # pprint(response.json())
# os.mkdir("todos")
# data = response.json()
# print(data)
# os.chdir("todos")
# for todo in data:
#   with open(f"{todo['id']}.txt", "w") as f:
#     f.write(f"Title: {todo['title']}\n")
#     f.write(f"User Id: {todo['userId']}\n")

os.mkdir("users")
os.chdir("users")
url = 'https://jsonplaceholder.typicode.com/users'
response = httpx.get(url=url)
data = response.json()
for user in data:
  with open(f"{user['username']}", "w") as f:
    f.write(f"Name: {user['name']}\n")
    f.write(f"Email: {user['email']}\n")