import requests

print(requests.__version__)

print(requests.get("http://google.com/").status_code)

script_url = "https://raw.githubusercontent.com/maharshmellow/404/master/labs/1/script.py"

print(requests.get(script_url).content)
