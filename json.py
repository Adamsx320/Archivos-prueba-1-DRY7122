import json

with open('myfile.json') as json_file:
    ourjson = json.load(json_file)

print("Token", ourjson[token])
print("Tiempo restante antes de que caduque el token:", ourjson["expiry_time"])

