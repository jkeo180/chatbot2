import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as file:
            return json.load(file)
    return []


def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=4)


memory = load_memory()

while True:
    user_input = input("User: ")
    memory.append({"role": "user", "content": user_input})

    # Simulate assistant response (replace with actual model call)
    assistant_response = f"Echo: {user_input}"
    print(f"Assistant: {assistant_response}")

    memory.append({"role": "assistant", "content": assistant_response})

    save_memory(memory)
