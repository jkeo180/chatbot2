import os
from pathlib import Path
import openai
# Step 1: Set the folder where your 4 WordPad files are
# Change this to your actual folder path!
docs_folder = Path(r"C:\User\11\chatbot2\docs")   # <-- CHANGE THIS!

# Example if it's on Desktop: Path(r"C:\Users\YourName\Desktop\my_docs")

# Step 2: List and load only .txt files (WordPad saves as .rtf or .txt — we'll handle both)
docs = []
for file_path in docs_folder.iterdir():
    if file_path.suffix.lower() in ['.txt', '.rtf']:
        try:
            # Try to read the file as plain text
            text = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # If that fails (common with .rtf), try latin-1 fallback
            text = file_path.read_text(encoding='latin-1')
        
        docs.append({
            "filename": file_path.name,
            "text": text.strip()
            })
        print(f"Loaded: {file_path.name} — {len(text)} characters")
embeddings = [] 
for doc in docs: 
    text = doc['text'] 
    response = openai.embeddings.create(input=text, model='text-embedding-3-small') 
    vector = response.data[0].embedding 
    embeddings.append(vector)
    print(f"Embedded '{doc['filename']}': {len(vector)}-dim")
print(f"\nTotal documents loaded: {len(docs)}")

# Step 3: Quick check — print first 200 characters of each
for doc in docs:
    print(f"\n--- {doc['filename']} ---")
    print(doc['text'][:200] + "...")