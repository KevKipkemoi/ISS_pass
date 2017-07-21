import requests


#check if it's over Eldoret
parameters = {"lat": 0.5143, "lon": 35.2698}
#current location
current_location = requests.get("http://api.open-notify.org/iss-now.json")

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(current_location)
print(response.content)
