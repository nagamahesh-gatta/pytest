import pytest
import requests

import source.Service as myservice
import unittest.mock as mock


@mock.patch("source.Service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):

    mock_get_user_from_db.return_value = "Alice"
    user_name = myservice.get_user_from_db(1)

    assert user_name == "Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):

    mock_response = mock.Mock()
    mock_response.status_code == 200
    mock_response.json.return_value = {"id":1, "name":"Leanne Graham"}
    mock_get.return_value = mock_response
    data = myservice.get_user()

    assert data == {"id":1, "name":"Leanne Graham"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code == 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        myservice.get_user()