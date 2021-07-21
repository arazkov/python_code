 
import json
from requests import get

#111111111111

with open('exercises_balls.json', 'r') as q:
    base = json.loads(q.read())

#222222222222222

base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
# print(type(base))

with open('data.json', 'w') as f:
  json.dump(base, f, indent=4, ensure_ascii=False)
