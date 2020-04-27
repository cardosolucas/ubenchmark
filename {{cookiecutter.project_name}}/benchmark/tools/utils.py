import time
import os
import gzip
import pickle
import joblib
from abc import ABC, abstractmethod

def get_time():
    return time.time()

def calculate_time(initial_time):
    return time.time() - initial_time

def check_path_or_create():
    project_folder = os.path.join(os.getcwd(), '.blobs')
    if not os.path.exists(project_folder):
        os.makedirs(project_folder)
    return project_folder

class AbstractSerializer(ABC):
    def __init__(self):
        pass

    def dump(self, obj, name):
        pass

    def load(self, name):
        pass

class DefaultSerializer(AbstractSerializer):
    def __init__(self):
        pass

    def dump(self, obj, name):
        filename = os.path.join(check_path_or_create(), name)
        with gzip.open(filename, "wb") as f:
            pickle.dump(obj, f)

    def load(self, name):
        filename = os.path.join(check_path_or_create(), name)
        with gzip.open(filename, "rb") as f:
            return pickle.load(f)

class JoblibSerializer(AbstractSerializer):
    def __init__(self):
        pass

    def dump(self, obj, name):
        filename = os.path.join(check_path_or_create(), name)
        joblib.dump(obj, filename)

    def load(self, name):
        filename = os.path.join(check_path_or_create(), name)
        ser_obj = joblib.load(filename, mmap_mode='r')
        return ser_obj