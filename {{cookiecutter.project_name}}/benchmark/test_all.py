import unittest.mock as mock

from tools.utils import DefaultSerializer
from tools.utils import JoblibSerializer
from tools.utils import get_time, calculate_time
from batch import run_preprocess
from batch import run_training
from online import post_predict

class PickableObject(object):
    def some_method(self, some_parameter):
        pass

@mock.patch('tools.utils.pickle.dump')
@mock.patch('tools.utils.gzip.open')
def test_default_serializer(pickle_dump, gzip_open):
    path_create = mock.MagicMock(return_value = '/path/to/artifact')
    with mock.patch('tools.utils.check_path_or_create', path_create, create=True):
        serializer = DefaultSerializer()
        p_obj = PickableObject()
        serializer.dump(p_obj, 'obj')

    path_create.assert_called_once()

@mock.patch('tools.utils.joblib.dump')
@mock.patch('tools.utils.gzip.open')
def test_joblib_serializer(joblib_dump, gzip_open):
    path_create = mock.MagicMock(return_value = '/path/to/artifact')
    with mock.patch('tools.utils.check_path_or_create', path_create, create=True):
        serializer = JoblibSerializer()
        p_obj = PickableObject()
        serializer.dump(p_obj, 'obj')

    path_create.assert_called_once()

def test_get_time():
    assert isinstance(get_time(), float)

def test_calculate_time():
    mocked_float = 0.1
    assert isinstance(calculate_time(mocked_float), float)

@mock.patch('batch.get_time')
@mock.patch('batch.calculate_time')
@mock.patch('batch.preprocess')
def test_run_preprocess(get_time, calculate_time, preprocess):
    serializer = mock.MagicMock()
    with mock.patch('batch.serializer', serializer, create=True):
        run_preprocess()

    preprocess.assert_called_once()
    get_time.assert_called_once()
    calculate_time.assert_called_once()

@mock.patch('batch.get_time')
@mock.patch('batch.calculate_time')
@mock.patch('batch.training')
def test_run_training(get_time, calculate_time, training):
    serializer = mock.MagicMock()
    with mock.patch('batch.serializer', serializer, create=True):
        run_training()

    training.assert_called_once()
    get_time.assert_called_once()
    calculate_time.assert_called_once()

@mock.patch('online.get_time')
@mock.patch('online.calculate_time')
@mock.patch('online.predict')
def test_online_prediction(get_time, calculate_time, predict):
    request = mock.MagicMock()
    json = mock.MagicMock()
    with mock.patch('online.request', request, create=True): 
            with mock.patch('online.json', json, create=True):
                post_predict()

    predict.assert_called_once()
    get_time.assert_called_once()
    calculate_time.assert_called_once()