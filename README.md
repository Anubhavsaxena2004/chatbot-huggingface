# Local Hugging Face Chatbot (CLI)

A simple command-line chatbot using a small Hugging Face text generation model. Maintains short-term memory for coherent multi-turn conversations.

## Features
- Loads a small language model locally (default: distilgpt2)
- Maintains a sliding window of recent conversation turns
- Robust CLI: accepts continuous input, exits on `/exit`
- Modular code structure

## Setup Instructions

1. **Clone the repository and navigate to the folder:**
   ```bash
   cd "gk chatbot"
   ```
2. **Install dependencies:**
   ```bash
   pip install transformers
   ```

## How to Run

```bash
python interface.py
```

## Sample Interaction

```
Welcome to the Local Hugging Face Chatbot! Type /exit to quit.
User: What is the capital of France?
Bot: The capital of France is Paris.
User: And what about Italy?
Bot: The capital of Italy is Rome.
User: /exit
Exiting chatbot. Goodbye!
```

## File Structure
- `model_loader.py` – Model and tokenizer loading
- `chat_memory.py` – Memory buffer logic
- `interface.py` – CLI loop and integration 