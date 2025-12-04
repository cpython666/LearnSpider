from curl_cffi import requests
# import requests
# response = requests.get("https://www.walmart.com/search?q=keyboard")
response = requests.get("https://www.walmart.com/search?q=keyboard", impersonate="chrome")
print(response.text)
print(response)