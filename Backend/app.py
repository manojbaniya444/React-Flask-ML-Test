from flask import Flask, request, jsonify
import numpy as np 
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model_pickle=pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    response = {
        'message': 'Welcome to the home route!'
    }


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Example: Extracting a specific value from the data
    value1 = data.get('Sepal_Length')
    value2 = data.get('Sepal_Width')
    value3 = data.get('Petal_Length')
    value4 = data.get('Petal_Width')

    values = [float(value1),float(value2),float(value3),float(value4)]
    features=[np.array(values)]

    prediction=model_pickle.predict(features)

    # Convert the prediction ndarray to a list
    prediction = prediction.tolist()

    # Example: Generating a response
    response = {
       "prediction": prediction
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
