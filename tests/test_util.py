import pytest
from obpy import util


@pytest.fixture
def data_without_none_values():
    return {
        'cities': 60,
        'countries': 20,
        'providers': 17,
        'stations': 6200
    }


@pytest.fixture
def data_with_none_values():
    return {
        'cities': 60,
        'countries': 20,
        'providers': 17,
        'stations': 6200,
        'noneKey': None
    }


def test_data_is_a_dict(data_without_none_values):
    ''' Check returned data is a dict. '''

    data = util.remove_none_values_from_dict(data_without_none_values)
    assert isinstance(data, dict) == True


def test_dict_has_no_none_values(data_without_none_values):
    ''' Check dict has not None values. '''

    data = util.remove_none_values_from_dict(data_without_none_values)
    for _, value in data.items():
        assert value is not None


def test_dict_has_none_values(data_with_none_values):
    ''' Check dict has None values. '''

    for _, value in data_with_none_values.items():
        if not value:
            assert value is None
