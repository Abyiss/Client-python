import requests


s = requests.Session()

print(s.get('http://169.63.179.247/v1/exchanges').json())
