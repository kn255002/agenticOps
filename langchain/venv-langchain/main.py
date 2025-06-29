# main.py
from agent_core.reader import read_text_file
from agent_core.parser import parse_task
from agent_core.executor import run_ansible

# Read input
text = read_text_file("data/sample_ticket.txt")

# Parse instruction using LLM
task = parse_task(text)

# Execute task
print("Its going to create user:\n", task['username'])
print("Target Machines:\n", task['machines'])


#result = run_ansible(task['username'], task['machines'])
#print("Ansible Output:\n", result)
