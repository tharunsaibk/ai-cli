import subprocess

def run_command(command):
    reponse = subprocess.run(command, shell=True, capture_output=True, text=True)
    if reponse.returncode == 0:
        return reponse.stdout.strip()   
    else:
        return f"Error: {reponse.stderr.strip()}"