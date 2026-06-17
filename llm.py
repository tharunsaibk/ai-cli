import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def is_safe_command(cmd: str) -> bool:
    dangerous_keywords = [
        "rm", "sudo", "shutdown", "reboot", "mkfs", "dd",
        ":(){", "chmod 777", "kill -9"
    ]
    return not any(word in cmd for word in dangerous_keywords)


def prompt_to_command(user_input: str) -> str:
    prompt = f"""
You are a CLI command generator.

Convert the user request into a  valid Mac/Linux shell command and it should be able to handle commands with options too.

Rules:
- Output ONLY the command (no explanation, no markdown)
- Prefer safe commands: ls, tree, pwd, cat, echo, find, grep
- If unclear, guess safest possible command
- NEVER use destructive commands (rm, sudo, shutdown, mkfs, dd)

User request: {user_input}
"""

    response = model.generate_content(prompt)
    cmd = response.text.strip()

    if not is_safe_command(cmd):
        return "Blocked - unsafe command : " + cmd

    return cmd