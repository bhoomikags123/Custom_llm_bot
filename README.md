Zaara 🤖

Zaara is a simple AI chatbot built with Streamlit and powered by Groq's blazing-fast LLM inference API. It's designed as a general-purpose assistant with a specialization in coding, algorithms, and programming help.

Features-

💬 Clean, chat-style interface using Streamlit's native chat components

⚡ Powered by Groq's openai/gpt-oss-120b model for fast responses

🧠 Persistent conversation history within a session

🎨 Custom gradient-themed UI

Tech Stack

Streamlit — Web app framework

Groq — LLM inference API

Getting Started-

Prerequisites-

1.Python 3.8+

2.A Groq API key

Installation-

1.Install dependencies:

bash-

 pip install -r requirements.txt
   
2.Set your Groq API key as an environment variable (recommended over hardcoding it):

bash-

export GROQ_API_KEY="your-api-key-here"
   
3.Update llm_prompt.py to read the key from the environment:

   import os
   
   client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
   
Running the App-

bash-

streamlit run llm_prompt.py

The app will open in your browser at http://localhost:8501.

Usage-

Type your question or prompt into the chat input box at the bottom of the screen. Zaara will respond using the Groq-hosted LLM, and your conversation history will persist for the duration of the session.

⚠️ Security Note-

Never commit real API keys to source control. Use environment variables or a .env file (added to .gitignore) to keep credentials out of your repository.
