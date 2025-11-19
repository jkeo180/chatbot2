from openai import OpenAI
import os
from dotenv import load_dotenv
from memory import add_short_term, get_short_term_messages, remember_fact, recall_fact, append_memory_event

# Load environment variables
load_dotenv()

# Initialize client (use your real API key or os.getenv)
client = OpenAI(api_key="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")

# Chat history starts empty
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
# load a fact (optional)
user_name = recall_fact("name")
if user_name:
    history.append({"role":"system", "content": f"User's name is {user_name}."})

print("Chatbot ready. Type 'quit' to exit, 'remember:' to store a fact, 'recall:' to get a fact.")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit"):
        break

    # quick local commands
    if user_input.startswith("remember:"):   # e.g. remember: favorite_color=blue
        try:
            body = user_input[len("remember:"):].strip()
            k, v = body.split("=", 1)
            remember_fact(k.strip(), v.strip())
            print("Saved!")
        except Exception as e:
            print("Format: remember:key=value")
        continue

    if user_input.startswith("recall:"):  # recall: favorite_color
        k = user_input[len("recall:"):].strip()
        print("Recall:", recall_fact(k, "Not found"))
        continue

    # normal convo flow
    history.append({"role":"user", "content": user_input})
    add_short_term("user", user_input)

    # Build messages that include short-term context
    short_context = get_short_term_messages()
    # We combine: system + long history (optional) + short-term to keep context small
    messages = [{"role":"system", "content":"You are a helpful coding buddy."}]
    messages.extend(short_context)  # short_context items are dicts with role+content

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        reply = response.choices[0].message.content
        print("Bot:", reply)
        add_short_term("assistant", reply)
        append_memory_event({"user": user_input, "assistant": reply})
    except Exception as e:
        print("Error:", e)
print("Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Add the user message
    messages.append({"role": "user", "content": user_input})

    # Get the assistant's response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4-turbo"
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print("Bot:", bot_reply)

    # Add the assistant reply to the history
    messages.append({"role": "assistant", "content": bot_reply})



