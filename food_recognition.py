import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

def load_model():
    return MobileNetV2(weights='imagenet')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def recognize_food(model, img_path):
    preprocessed_img = preprocess_image(img_path)
    predictions = model.predict(preprocessed_img)
    top_prediction = decode_predictions(predictions, top=1)[0][0]
    return top_prediction[1], top_prediction[2]  # Returns (class_name, confidence)

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     model = load_model()
#     img_path = 'path_to_your_food_image.jpg'
#     class_name, confidence = recognize_food(model, img_path)
#     print(f"Recognized food: {class_name} (confidence: {confidence:.2f})")