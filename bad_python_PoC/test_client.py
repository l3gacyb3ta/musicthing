import requests

# start the buying process
resp = requests.get("http://127.0.0.1:8080/heaven_pierce_her/ultrakill/buy").json()
session = resp["sessionid"]

requests.post("http://127.0.0.1:8080/test_buy_url", json={"sessionid": session})
x = requests.get("http://127.0.0.1:8080/heaven_pierce_her/ultrakill/deliver", json={"sessionid": session})
print(x)