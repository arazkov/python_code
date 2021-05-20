 
import json
from requests import get

base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
# print(type(base))

with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(base, f, indent=4)
