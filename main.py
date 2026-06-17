from llm import prompt_to_command
from executor import run_command

prompt =input("You: ")

command = prompt_to_command(prompt)
print(f"Generated command: {command}")
if(input("Do you want to execute this command? (y/n): ").lower() == 'y'):
    output = run_command(command)
    print(output)