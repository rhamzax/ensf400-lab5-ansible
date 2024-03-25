import ansible_runner
import requests
import os

os.environ['ANSIBLE_CONFIG'] = os.path.join(".", 'ansible.cfg')

r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml', playbook='hello.yml')

print("Playbook Execution Status:")
print("Status:", r.status)
print("RC:", r.rc)

print("\nVerifying Node:")
http = "http://0.0.0.0"

try:
    response = requests.get(http)
    if response.status_code == 200:
        print(f"NodeJS server at {http} is reachable and responding correctly.")
    else:
        print(f"NodeJS server at {http} returned status code: {response.status_code}")
except requests.ConnectionError:
    print(f"NodeJS server at {http} is unreachable.")
