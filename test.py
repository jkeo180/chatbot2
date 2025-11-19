import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
os.getcwd()
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Debug print — just to check if the key is found
if not api_key:
    print("❌ No API key found. Check your .env file name and path.")
    exit()
else:
    print(f"✅ Found API key starting with: {api_key[:8]}...")

# Initialize client
client = OpenAI(api_key=api_key)

# Try a simple API call
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hello!"}]
    )
    print("✅ API call succeeded!")
    print("Response:", response.choices[0].message.content)

except Exception as e:
    print("❌ API call failed.")
    print("Error:", e)

print("Loaded key:", os.getenv("OPENAI_API_KEY"))
#print(os.getcwd())
#print(os.listdir())
