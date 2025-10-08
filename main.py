import requests

response = requests.get("https://quotes.toscrape.com/")
print(response)

if response.status_code == 200:
    print("All Good")
else:
    print("Error")
# print(response.content)