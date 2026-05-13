import requests

response = requests.get("https://api.github.com")
print(f"Connection Status Code: {response.status_code}") 
