import subprocess
import requests
import json

def service_url(servicename, url_suffix):
    p = subprocess.run(['minikube', 'service', servicename, '--url'], capture_output=True)
    if p.returncode!= 0:
        print(f"Error executing 'minikube service': {p.stderr}")
        return None
    raw_url = str(p.stdout.decode()).strip()
    return raw_url + url_suffix

#url = 'http://localhost:5000/hash'
url = service_url('hash-service', '/hash')
headers = {'Content-Type': 'application/json'}
data = {'hash': 'hash data to convert'}

# Invia la richiesta GET con i dati JSON nel corpo
print(url)
response = requests.get(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
