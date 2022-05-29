import requests

res = requests.get("https://api.postalpincode.in/pincode/608001")
print(res.json())
