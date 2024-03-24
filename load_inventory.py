import ansible_runner
ansible_runner.get_inventory(action='list', inventories=['/workspaces/ensf400-lab5-ansible/hosts.yml'])
ansible_runner.get_inventory(action='graph', inventories=['/workspaces/ensf400-lab5-ansible/hosts.yml'])
# ansible_runner.get_inventory(action='host', inventories=['/workspaces/ensf400-lab5-ansible/hosts.yml'], host='managedhost-app-1')