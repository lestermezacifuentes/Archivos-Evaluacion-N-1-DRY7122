import json
import yaml

with open ('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

print (ourjson)
print("El token de acceso es: {}".format(ourjson['access_token']))
print("Se expira el toxen en {} seconds.".format(ourjson['expires_in']))
# Fill in this file with the code from parsing JSON exercise
