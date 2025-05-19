import requests

res = requests.get('http://127.0.0.1:5000/admin_get_card_structure')
print(res.text)