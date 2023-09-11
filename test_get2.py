import requests

response = requests.get("https://reqres.in/api/users?page=2")#200
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/users/2")#200
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/users/23")#404
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/unknown")#200
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/unknown/2")#200
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/unknown/23")#404
print(response)
print(response.headers)
print(response.text)

json = {"name": "morpheus","job": "leader"}
response = requests.post("https://reqres.in/api/users",data=json)#201
print(response)
print(response.headers)
print(response.text)

json = {"name": "morpheus","job": "zion resident"}
response = requests.put("https://reqres.in/api/users/2",data=json)#200
print(response)
print(response.headers)
print(response.text)

json = {"name": "morpheus","job": "zion resident"}
response = requests.patch("https://reqres.in/api/users/2",data=json)#200
print(response)
print(response.headers)
print(response.text)

response = requests.delete("https://reqres.in/api/users/2",data=json)#204
print(response)
print(response.headers)
print(response.text)

json = {"email": "eve.holt@reqres.in","password": "pistol"}#200
response = requests.post("https://reqres.in/api/register",data=json)
print(response)
print(response.headers)
print(response.text)

json = {"email": "sydney@fife"}
response = requests.post("https://reqres.in/api/register",data=json)#400
print(response)
print(response.headers)
print(response.text)

json = {"email": "eve.holt@reqres.in","password": "cityslicka"}#200
response = requests.post("https://reqres.in/api/login",data=json)
print(response)
print(response.headers)
print(response.text)

json = {"email": "peter@klaven"}#400
response = requests.post("https://reqres.in/api/login",data=json)
print(response)
print(response.headers)
print(response.text)

response = requests.get("https://reqres.in/api/users?delay=3")#200
print(response)
print(response.headers)
print(response.text)

