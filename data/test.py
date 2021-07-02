import json
import requests

var = "00602"

url = "https://www.zipcodeapi.com/rest/DemoOnly00TfM2ygeeH9G6rB1l65HfBzyTZyAAhXtIfyNbn3qiGWHgZJCm8mxVSm/radius.csv/"+var+"/50/miles?minimal"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)





# import json
  

# with open('sample.json') as f:
#   data = json.load(f)
  
# print(data["configuration"][0]["questions"][1])
# # print(data["orgId"])