
# **ConsumWise - AI-powered Food Label Scanner**

## **Overview**
**ConsumWise** is an AI-driven application that helps users make informed decisions about the foods they consume. By scanning food labels with a smartphone camera, the app extracts and analyzes ingredients, allergens, and health impacts. With personalized health recommendations based on dietary preferences and goals, ConsumWise empowers users to make healthier choices.

---

## **Table of Contents**
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [How it Solves the Problem](#how-it-solves-the-problem)
- [Why Use GenAI](#why-use-genai)
- [Future Opportunities](#future-opportunities)

---

## **Features**
- **Label Scanning**: Scan food labels using a smartphone camera to extract barcodes and nutritional text.
- **Product Information Retrieval**: Fetches detailed product information using external APIs (e.g., Open Food Facts).
- **AI-powered Ingredient Analysis**: Uses AI to analyze ingredients for allergens, additives, and health impacts.
- **Personalized Health Recommendations**: Tailors recommendations based on dietary restrictions and health goals.
- **User Profiles & Scan History**: Users can create profiles to store dietary preferences and view their scan history.

---

## **Tech Stack**
- **Frontend**: React.js / React Native
- **Backend**: Node.js with Express.js
- **AI Layer**: Python (TensorFlow/PyTorch)
- **Databases**: MongoDB, PostgreSQL
- **Cloud Hosting**: AWS / Google Cloud
- **External APIs**: Open Food Facts, Barcode Lookup API

---

## **System Architecture**
### **Frontend**
- React.js (Web) / React Native (Mobile) for label scanning, displaying product details, and managing user profiles.
  
### **Backend**
- Node.js with Express.js for API routing, connecting to external databases, and managing user data.
  
### **AI Layer**
- Python-based AI model analyzes ingredients, detects allergens, and offers health impact assessments.

### **Databases**
- **MongoDB** stores user profiles, dietary preferences, and scan history.
- **PostgreSQL** holds structured product data like ingredients and nutritional information.

### **Cloud Hosting**
- Hosted on **AWS** or **Google Cloud** with external APIs integrated for real-time product info.

### **Security**
- **OAuth 2.0** for authentication, **JWT** for token-based access, and **SSL/TLS** for encrypted data transmission.

---

## **Installation**

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Oblivious19/ConsumeWise.git
   \`\`\`
   
2. Navigate to the project folder:
   \`\`\`bash
   cd ConsumeWise
   \`\`\`

3. Install dependencies for both frontend and backend:
   \`\`\`bash
   npm install
   \`\`\`

4. Configure your environment variables:
   - Create a `.env` file in the root folder and add your API keys, database URLs, and other environment-specific variables.
   
5. Start the development server:
   \`\`\`bash
   npm run dev
   \`\`\`

---

## **Usage**

1. **Scan a Label**: Use the app to scan food labels and extract product information via barcodes or text.
2. **Analyze Ingredients**: AI processes ingredients and highlights potential allergens, harmful additives, and nutritional details.
3. **Get Health Recommendations**: Receive personalized health recommendations based on your profile and dietary preferences.

---

## **How it Solves the Problem**

Consumers struggle with understanding the health implications of packaged food due to unclear labeling. **ConsumWise** addresses this challenge by:
- **AI-powered analysis**: Automatically interpreting complicated ingredient lists.
- **Personalized recommendations**: Tailored advice based on user preferences and health goals.
- **Real-time scanning**: Providing instant feedback on scanned food items.

---

## **Why Use GenAI**

**GenAI** (Generative AI) is the optimal solution because:
- It efficiently processes large and complex ingredient lists, identifying hidden risks.
- It provides personalized health insights tailored to each user’s dietary needs and restrictions.
- It continually learns from new data to offer up-to-date and accurate recommendations.

---

## **Future Opportunities**

- **Expanded Product Database**: Integration with more product databases globally for comprehensive food item coverage.
- **Advanced Health Insights**: AI-driven suggestions for healthier alternatives.
- **Allergy Alerts**: Real-time alerts for potential allergen exposure.
- **Wearable Integration**: Sync data with wearables (e.g., fitness trackers) for holistic health tracking.

---

## **Contributing**
We welcome contributions to improve **ConsumWise**. Please submit pull requests or open issues to help enhance the project.

---

## **License**
This project is licensed under the MIT License.

---

## **Contact**
For questions or suggestions, reach out at: [Shreya Ojha](shreyaojha2@gmail.com).
