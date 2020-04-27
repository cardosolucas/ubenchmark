#!/usr/bin/env python3

from tools.log import get_logger
from tools.utils import get_time, calculate_time
from tools.utils import DefaultSerializer

from predict import predict
from preprocess import preprocess
from training import training

serializer = DefaultSerializer()
logger = get_logger('batch')

def run_preprocess():
    initial_time = get_time()
    logger.info('Preprocess start.')
    data = preprocess()
    serializer.dump(data, 'data')
    logger.info('Preprocess end: ' + str(calculate_time(initial_time)) + ' seconds.')

def run_training():
    initial_time = get_time()
    logger.info('Training start.')
    data = serializer.load('data')
    model = training(data)
    serializer.dump(model, 'model')
    logger.info('Training end: ' + str(calculate_time(initial_time)) + ' seconds.')

run_preprocess()
run_training()