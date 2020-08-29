import requests

r = requests.post('http://localhost:7000/health_services/get_true_value')
print(r.text)