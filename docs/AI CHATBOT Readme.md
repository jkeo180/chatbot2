# **AI CHATBOT Readme**



**1. What is this?**

AI Chatbot

**2. Why should I care?**

I built this chatbot on my journey to build a private uncensored customizable chatbot, this is a prototype

**3. How do I run it without breaking my soul?**

* Clone this repo
* setup virtual environment
* install dependencies
* create environmental variables
* run chatbot in bash



---



##### \## 🧠 Chatbot with Memory \& Tools

##### 

##### \### Overview



This project is a \*\*Python-based chatbot built using the OpenAI API\*\*.

It supports conversational memory and is designed with extensibility, security, and maintainability in mind.



The goal of this project is to explore \*\*real-world chatbot architecture\*\*, not just basic prompt-response demos.



---



##### \## ✨ Features



\* Conversational chatbot using OpenAI models

\* Short-term memory handling

\* Modular code structure

\* Designed for future tool integration (memory, evaluation, external tools)

\* Focus on reliability and reducing common failure modes (e.g. echoing)



---



##### \## 🛠️ Tech Stack



\* Python 3.10+

\* OpenAI API

\* Virtual environments

\* Standard Python tooling (requests, dotenv, etc.)



---



##### \## 📁 Project Structure



```text

chatbot/

├── py\_cache

&nbsp;        ├──memory.cpython

&nbsp;        ├──short\_term\_memory.cpython    

├── vscode

&nbsp;        ├──settings.json          

├── docs

&nbsp;	├──Readme.md-Your are here

&nbsp;	├──Copy2Opensource.txt

&nbsp;	├──Search.py           

├── memory

&nbsp;	├──pycache

&nbsp;	├──long\_term\_memory.py

&nbsp;	├──memory.json

&nbsp;	├──short\_term\_memory.py          

├── tools

&nbsp;	├──image\_generation.py

&nbsp;	├──reminder\_bot.py

&nbsp;	├──SpeechtoText.py

&nbsp;	├──TexttoSpeech.py

&nbsp;	├──Weatherbot.py

&nbsp;	├──Webscraper.py

├──Venv

&nbsp;	├──Main

&nbsp;		├──embeddings

&nbsp;		├──faceUI.py

&nbsp;		├──Main.py

└── Scripts

&nbsp;	├──.env

&nbsp;	├──.json

&nbsp;	├──memory.json

&nbsp;	├──test.py

```

---



##### \## 🚀 Getting Started



\### 1. Clone the Repository



```bash

git clone https://github.com/yourusername/your-repo-name.git

cd your-repo-name

```



\### 2. Set Up a Virtual Environment



```bash

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate

```



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 4. Environment Variables



Create a `.env` file:



```text

OPENAI\_API\_KEY=your\_api\_key\_here

```



---



\## ▶️ Running the Chatbot



```bash

python main.py

```



You should see a prompt allowing you to interact with the chatbot via the terminal.



---



##### \## 🧠 Memory Design (High-Level)



\* Short-term memory is stored per session

\* Messages are appended and trimmed to stay within token limits

\* Architecture allows for future long-term or vector-based memory





---



##### \## 🔐 Security Considerations



\* API keys are loaded via environment variables

\* Input is validated before being sent to the model

\* Designed to reduce prompt injection and misuse risks



---



##### \## 🧪 Known Limitations



\* No persistent long-term memory yet

\* CLI-only interface

\* Tool system is basic and under active development



---



##### \## 🔭 Roadmap



\* Add long-term memory storage

\* Add tool calling (reminders, retrieval, evaluation)

\* Improve logging and error handling

\* Add UI (Streamlit or web frontend)



---



##### \## 📌 Why This Project Exists



This chatbot is part of a broader effort to \*\*learn AI systems properly\*\*, including:



\* memory management

\* tool integration

\* security concerns

\* maintainable code design



---



##### \## 📄 License



MIT 



---



