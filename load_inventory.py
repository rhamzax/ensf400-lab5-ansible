import ansible_runner
import os

os.environ['ANSIBLE_CONFIG'] = os.path.join(".", 'ansible.cfg')

r = ansible_runner.run(private_data_dir='.', inventory='hosts.yml', host_pattern='all', module='ping')


print("Hosts:")
for event in r.events:
    if event['event'] == 'runner_on_ok':
        host = event['event_data']['host']
        ansible_facts = event['event_data']['res']['ansible_facts']
        ip = ansible_facts.get('ansible_host', 'IP address not found')
        groups = ansible_facts.get('group_names', [])
        print(f"Name: {host}, Groups: {', '.join(groups)}, IP: {ip}")


print("\nPinging Hosts:")
for event in r.events:
    if event['event'] == 'runner_on_ok':
        host = event['event_data']['host']
        ping_result = event['event_data']['res']['ping']
        print(f"Host: {host}, Result: {ping_result}")