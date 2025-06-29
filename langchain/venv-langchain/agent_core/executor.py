# agent_core/executor.py
import subprocess

def run_ansible(username, machines):
    inventory_file = 'configs/inventory.ini'
    cmd = [
        "ansible-playbook",
        "playbooks/create_user.yml",
        "-i", inventory_file,
        "--extra-vars", f"username={username}",
        "--limit", ",".join(machines)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
