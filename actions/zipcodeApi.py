import requests, json


def getZipRadius(Zipcode):

    url = "https://www.zipcodeapi.com/rest/DemoOnly00TfM2ygeeH9G6rB1l65HfBzyTZyAAhXtIfyNbn3qiGWHgZJCm8mxVSm/radius.json/"+Zipcode+"/50/mile"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.dumps(response.json(), indent = 4)            
    with open("ZipData.json", "w") as outfile:
        outfile.write(json_object)
    print(response.json())


