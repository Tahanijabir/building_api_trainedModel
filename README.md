# building_api_trainedModel
A step-by-step guide on how to build a REST API for a trained model using TensorFlow and Flask.

## Step 1: Install Necessary Libraries
First, you need to install the necessary libraries. You can do this by running the following command in your terminal:

```bash
pip install flask tensorflow
```

## Step 2: Import Libraries
Next, import the necessary libraries in your Python script:

```python
from flask import Flask, request
from tensorflow.keras.models import load_model
import numpy as np
```

## Step 3: Load Your Trained Model
Load your trained model using TensorFlow's `load_model` function:

```python
model = load_model('your_model.h5')
```
Replace `'your_model.h5'` with the path to your trained model file.

## Step 4: Create a Flask App
Create a Flask app instance:

```python
app = Flask(__name__)
```

## Step 5: Define a Route for Your API
Define a route for your API that listens for POST requests. This is where you will receive the input data for your model:

```python
@app.route('/predict', methods=['POST'])
```

## Step 6: Create a Function to Handle Requests
Create a function that gets the data from the POST request, converts it into a numpy array, feeds it into the model for prediction, and then returns the prediction as a response:

```python
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input'])
    prediction = model.predict([input_data])
    output = prediction[0]
    return str(output)
```

## Step 7: Run the Flask App
Finally, run the Flask app:

```python
if __name__ == '__main__':
    app.run(port=5000, debug=True)
```

This will start a local server at `localhost:5000`. You can make POST requests to `localhost:5000/predict` to get predictions from your model.

