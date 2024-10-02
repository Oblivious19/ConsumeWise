import cv2
import pytesseract
import numpy as np
from PIL import Image
import logging
import re
import string

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        logger.error(f"Failed to load image: {image_path}")
        return None, None
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
    thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    return image, thresh

def extract_text_from_image(image):
    return pytesseract.image_to_string(image, config='--psm 11 --oem 3 -l eng')

def clean_text(text):
    text = re.sub(r'[^\w\s.,%]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return ' '.join(word.capitalize() for word in text.split())

def find_best_match(text, keywords, threshold=0.6):
    text_lower = text.lower()
    best_match = None
    best_score = 0
    for keyword in keywords:
        score = sum(1 for word in keyword.lower().split() if word in text_lower)
        if score > best_score:
            best_score = score
            best_match = keyword
    return best_match if best_score / len(keyword.split()) >= threshold else None

def extract_numeric_value(text, keyword):
    pattern = r'{}.*?(\d+(?:\.\d+)?)\s*(?:g|ml|oz|lb|kcal)?'.format(re.escape(keyword))
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1) if match else None

def process_package_label(image_path):
    try:
        original_image, preprocessed_image = preprocess_image(image_path)
        
        if original_image is None or preprocessed_image is None:
            logger.error("Failed to load or preprocess image.")
            return {}
        
        full_text = extract_text_from_image(preprocessed_image)
        logger.info(f"Extracted full text: {full_text}")
        
        cleaned_text = clean_text(full_text)
        logger.info(f"Cleaned text: {cleaned_text}")
        
        product_info = {}
        
        # Brand name (look for known brands and common misspellings)
        known_brands = ['Doritos', 'Lays','Wingreens', 'Pringles', 'Cheetos', 'Tostitos', 'Dorites',]
        brand_match = find_best_match(cleaned_text, known_brands, threshold=0.5)
        if brand_match:
            product_info['brand'] = brand_match
        
        # Product category
        categories = ['Chips','Sauce', 'Snack', 'Biscuit', 'Cookie', 'Cereal', 'Pasta', 'Rice', 'Candy', 'Chocolate', 'Namkeen']
        category_match = find_best_match(cleaned_text, categories, threshold=0.5)
        if category_match:
            product_info['category'] = category_match
        
        # Flavor description (expanded and more flexible matching)
        flavors = ['Cheese', 'Nacho Cheese', 'Jalapeno', 'Spicy', 'Original', 'Barbecue', 'BBQ', 'Masala', 'Tandoori', 
                   'Sour Cream', 'Onion', 'Salt', 'Vinegar', 'Sweet Chili', 'Cool Ranch', 'Flamin Hot']
        flavor_match = find_best_match(cleaned_text, flavors, threshold=0.4)
        if flavor_match:
            product_info['flavor'] = flavor_match
        else:
            # If no exact match, look for combinations
            flavor_words = set(cleaned_text.lower().split()) & set(word.lower() for flavor in flavors for word in flavor.split())
            if flavor_words:
                product_info['flavor'] = ' '.join(flavor_words).capitalize()
        
        # Size or quantity information (more flexible matching)
        size_pattern = r'\b(\d+(?:\.\d+)?)\s*(g|oz|ml|l|lb)\b'
        size_match = re.search(size_pattern, cleaned_text, re.IGNORECASE)
        if size_match:
            product_info['size'] = size_match.group()
        
        # Nutritional information (more flexible matching)
        nutrients = ['Calories', 'Energy', 'Fat', 'Carbs', 'Sugar', 'Salt', 'Sodium', 'Protein']
        product_info['nutritional_info'] = {}
        for nutrient in nutrients:
            value = extract_numeric_value(cleaned_text, nutrient)
            if value:
                product_info['nutritional_info'][nutrient] = value
        
        # Look for percentage more
        percent_more = re.search(r'(\d+)%\s*more', cleaned_text, re.IGNORECASE)
        if percent_more:
            product_info['promotion'] = f"{percent_more.group(1)}% more"
        
        logger.info(f"Extracted product info: {product_info}")
        
        return product_info
    
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return {}

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\shrey\OneDrive\Desktop\WhatsApp Image 2024-09-03 at 19.06.05.jpeg'
    result = process_package_label(image_path)
    print(result)

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     image_path = r'C:\Users\shrey\OneDrive\Desktop\WhatsApp Image 2024-09-03 at 19.06.05.jpeg'
#       r'C:\Users\shrey\OneDrive\Desktop\71WQbGdcqNL._AC_UF1000,1000_QL80_.jpg'
# r'C:\Users\shrey\OneDrive\Desktop\images.jpg'
#     extracted_text = extract_text(image_path)
#     print("Extracted text:", extracted_text)