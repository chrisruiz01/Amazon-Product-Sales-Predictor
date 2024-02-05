import streamlit as st
import requests
import json

# MODEL_URL = 'http://localhost:8001/predict_probability'
MODEL_URL = 'http://amzdns.southcentralus.azurecontainer.io:8001/predict_probability'

st.title('Product Sales Performance Predictor')

st.markdown("""
**How to Use:**
1. **Enter Product Title**: Type the title of your Amazon product in the text box. Be as accurate as possible—include brand, model, and key descriptors.
2. **Get Predictions**: Click the 'Predict Sales Performance' button to estimate the sales potential of your product.
""")

with st.form(key='prediction_form'):
    input_text = st.text_input(label='Product Title')
    submit_button = st.form_submit_button(label='Predict Sales Performance')

if submit_button and input_text:
    data = json.dumps({"review": [input_text]})
    headers = {"Content-Type": "application/json"}

    response = requests.post(MODEL_URL, headers=headers, data=data)

    if response.status_code == 200:
        prediction = response.json()

        # Check the structure of prediction
        if isinstance(prediction, list) and len(prediction) == 1 and isinstance(prediction[0], list) and len(prediction[0]) == 1:
            # Access the nested list
            prediction_value = prediction[0][0]
            prediction_percentage = round(prediction_value * 100)
            message = f"Based on the provided product title, there is a {prediction_percentage}% probability that the product titled \"{input_text}\" will sell more than 100 units. Use this insight to optimize your product titles and improve sales potential."
        else:
            message = "The prediction format is not recognized."
        st.success(message)
    else:
        st.error(f'Failed to get prediction from the model. Status code: {response.status_code}')
        st.write("Debug: API response", response.json())  # Debug output

st.markdown("""
**Tips for Optimization**:
- **Reflect Key Features**: Include significant features that a potential customer might search for.
- **Brand and Model**: Always include the brand and model name for better recognition.
- **Descriptive Keywords**: Use keywords that accurately describe the product's unique qualities and uses.

Remember, the title is often a customer's first impression of your product—make it count!
""")
