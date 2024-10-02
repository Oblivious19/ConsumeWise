from transformers import pipeline

def get_nutritional_info(food_item):
    # Initialize the pipeline
    nlp = pipeline("text-generation", model="gpt2")
    
    # Generate prompt
    prompt = f"Provide nutritional information for {food_item}:"
    
    # Generate response
    response = nlp(prompt, max_length=100, num_return_sequences=1)
    
    return response[0]['generated_text']

# # Example usage uncomment to test
# if __name__ == "__main__":
#     food_item = "apple"
#     nutritional_info = get_nutritional_info(food_item)
#     print(nutritional_info)