from tests_wrapper import session
from tests_wrapper import assert_valid_schema
import json

tv_instance = 1396
api_key = '80d6c097716e6aebba3f7d9d84aa19fe'


def test_tv_id():

    #Arrange
    path = 'https://api.themoviedb.org/3/tv/%s' % tv_instance
    authentication = {'api_key': api_key}

    #Act
    response = session.get(path, params=authentication)
    json = response.json()
    created_by = json['created_by'][0]


    #Assert
    assert response.status_code == 200
    assert created_by['credit_id'] == '52542286760ee31328001a7b'


def test_tv_json():

    #Arrange
    path = 'https://api.themoviedb.org/3/tv/%s' % tv_instance
    authentication = {'api_key': api_key}

    #Act
    response = session.get(path, params=authentication)
    json_data = json.loads(response.content)


    #Assert
    assert_valid_schema(json_data, 'tv_response.json')