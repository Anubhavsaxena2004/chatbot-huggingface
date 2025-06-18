from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def load_model(model_name="gpt2"):
    """
    Loads a Hugging Face text generation pipeline with the specified model.
    Args:
        model_name (str): The name of the Hugging Face model to load.
    Returns:
        pipeline: A text-generation pipeline object.
    """
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Create pipeline with specific configuration
    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1  # Use CPU
    ) 