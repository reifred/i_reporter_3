from app import app
from tests.data_test import (
    valid_user2, valid_sign_in2, valid_admin, sign_in_admin)
import json


class GetToken:

    @staticmethod
    def get_user_token():
        response = app.test_client().post('/api/v1/auth/sign_up', json=valid_user2)
        response = app.test_client().post(
            '/api/v1/auth/sign_in', json=valid_sign_in2)
        token = json.loads(response.data)["data"][0]['token']
        return token

    @staticmethod
    def get_admin_token():
        response = app.test_client().post('/api/v1/auth/sign_up', json=valid_admin)
        response = app.test_client().post('/api/v1/auth/sign_in', json=sign_in_admin)
        token = json.loads(response.data)["data"][0]['token']
        return token
