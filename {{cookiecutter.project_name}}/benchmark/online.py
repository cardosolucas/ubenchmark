#!/usr/bin/env python3

from flask import Flask, json, request
import numpy as np

from tools.log import get_logger
from tools.utils import get_time, calculate_time
from tools.utils import DefaultSerializer

from predict import predict

logger = get_logger('online')

serializer = DefaultSerializer()

app = Flask(__name__)

MODEL = serializer.load('model')  

@app.route('/predict', methods=['POST'])
def post_predict():
    message_dict = request.json
    initial_time = get_time()
    logger.info('Prediction start.')
    prediction = predict(MODEL, message_dict['message'])
    logger.info('Prediction end: ' + str(calculate_time(initial_time)) + ' seconds.')
    return json.dumps(prediction), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)