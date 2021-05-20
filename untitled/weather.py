import json
from requests import get

ip = get('https://api.ipify.org').text
result_str = get(f'http://ip-api.com/json/{ip}?lang=ru').text
result = json.loads(result_str)
weather = get(f"http://wttr.in/{result['city']}?format=3").text
print("My public IP address is: {},\nMy city is: {}\nweather: {}".format(ip, result['city'], weather))
