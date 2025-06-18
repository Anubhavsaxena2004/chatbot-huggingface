from model_loader import load_model
from chat_memory import ChatMemory


def main():
    print("Welcome to the Local Hugging Face Chatbot! Type /exit to quit.")
    chatbot = load_model()
    memory = ChatMemory(window_size=5)
    
    # System prompt to guide the model
    system_prompt = "You are a helpful assistant that provides factual and accurate information. Please answer questions truthfully and concisely.\n\n"
    
    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break
            
        # Build prompt with memory and system prompt
        context = memory.get_context()
        prompt = system_prompt + context + f"User: {user_input}\nBot:"
        
        # Generate response with better parameters
        response = chatbot(
            prompt,
            max_new_tokens=100,
            num_return_sequences=1,
            temperature=0.6,  # Lower temperature for more focused responses
            top_p=0.9,
            do_sample=True,
            pad_token_id=chatbot.tokenizer.eos_token_id,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3
        )[0]["generated_text"]
        
        # Extract only the new response
        response = response[len(prompt):].strip().split("\n")[0]
        if not response:  # If response is empty, try again with different parameters
            response = chatbot(
                prompt,
                max_new_tokens=80,
                temperature=0.7,
                top_p=0.95,
                do_sample=True,
                pad_token_id=chatbot.tokenizer.eos_token_id
            )[0]["generated_text"][len(prompt):].strip().split("\n")[0]
            
        print(f"Bot: {response}")
        memory.add_turn(user_input, response)

if __name__ == "__main__":
    main() 