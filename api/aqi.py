import requests
import dotenv
import os
import sys


arg_city = "Yangon"

# sys.argv[0] is the name of the script itself
# sys.argv[1] is the first cmd line argument
if len(sys.argv) >= 2:
    arg_city = sys.argv[1]

dotenv.load_dotenv()
token = os.getenv("AIRQ_API_TOKEN")

airq_api_url = "http://api.waqi.info/feed/#city#/?token=#token#"

request_url = airq_api_url.replace("#city#", arg_city)
request_url = request_url.replace("#token#", token)

response = requests.get(request_url)
json_data = response.json()["data"]


if response.json()['status'] == "ok":
    print(f"{json_data['city']['name']} has current polution level {json_data['aqi']}")
else:
    print(f"{response.json()['data']}")

