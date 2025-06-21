from flask import Flask, render_template, request, jsonify, session
from model_loader import load_model
from chat_memory import ChatMemory
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Random secret key for session

# Initialize model
model = load_model()

# System prompt to guide the model
SYSTEM_PROMPT = "You are a helpful, knowledgeable, and concise AI assistant. Provide accurate and informative responses."

@app.route('/')
def index():
    # Initialize chat memory in session if not exists
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip()
    if not user_input:
        return jsonify({'response': 'No input provided.'})
    
    # Get chat history from session
    history = session.get('chat_history', [])
    memory = ChatMemory(window_size=5)
    
    # Load history into memory
    for user, bot in history:
        memory.add_turn(user, bot)
    
    # Build prompt with memory and system prompt
    context = memory.get_context()
    prompt = f"{SYSTEM_PROMPT}\n\n{context}User: {user_input}\nBot:"
    
    try:
        # Generate response
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Handle empty responses
        if not response_text:
            response_text = "I'm having trouble processing that. Could you rephrase your question?"
    except Exception as e:
        response_text = f"Error generating response: {str(e)}"
    
    # Add to history and update session
    history.append((user_input, response_text))
    
    # Keep only the last 5 messages (window_size)
    if len(history) > 5:
        history = history[-5:]
    
    session['chat_history'] = history
    
    return jsonify({'response': response_text})

@app.route('/reset', methods=['POST'])
def reset():
    memory.clear()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)