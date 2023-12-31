# -*- coding: utf-8 -*-
"""api_trainedModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tP7VMQQVMUDZ8cL9v8iIUAEyh_f0J3Xp
"""

from flask import Flask, request
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load_model('your_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json(force=True)

    # Convert data into numpy array
    input_data = np.array(data['input'])

    # Make prediction using model loaded from disk as per the data
    prediction = model.predict([input_data])

    # Take the first value of prediction
    output = prediction[0]

    return str(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)