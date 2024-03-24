import ansible_runner

def run_playbook(playbook):
    r = ansible_runner.run(playbook=playbook, inventory='/workspaces/ensf400-lab5-ansible/hosts.yml')
    return r

print(run_playbook('/workspaces/ensf400-lab5-ansible/hello.yml'))