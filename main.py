from food_recognition import load_model, recognize_food
from ocr import extract_text
from llm_nutritional_info import get_nutritional_info

def process_image(image_path):
    # Load the image recognition model
    model = load_model()
    
    # First, try OCR on all images
    text = extract_text(image_path)
    
    if text.strip():  # If OCR extracted some text
        # Use the first line of extracted text as the food item name
        food_item = text.split('\n')[0].strip()
        print(f"OCR extracted text: {food_item}")
    else:
        # If OCR didn't work, fall back to image recognition
        class_name, confidence = recognize_food(model, image_path)
        food_item = class_name
        print(f"Image recognition result: {food_item} (confidence: {confidence:.2f})")
    
    # Get nutritional information
    nutritional_info = get_nutritional_info(food_item)
    
    return food_item, nutritional_info

if __name__ == "__main__":
    # Example usage
    image_path = 'path_to_your_image.jpg'
    food_item, nutritional_info = process_image(image_path)
    print(f"Identified food item: {food_item}")
    print(f"Nutritional information: {nutritional_info}")