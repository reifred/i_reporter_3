from app import app
from tests.data_test import (
    user_short_pass,
    valid_user,
    user_invalid_phone,
    user_invalid_email,
    user_name_not_string,
    sign_wrong_password,
    sign_wrong_username,
    valid_sign_in
)
import unittest
import json


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_01_home(self):
        response = self.client.get("/api/v1/")
        self.assertEqual(200, response.status_code)
        self.assertIn("Welcome to api", str(response.data))

    def test_02_sign_up_without_JSON(self):
        response = self.client.post("/api/v1/auth/sign_up")
        self.assertEqual(400, response.status_code)

    def test_03_sign_in_without_JSON(self):
        response = self.client.post("/api/v1/auth/sign_in")
        self.assertEqual(400, response.status_code)

    def test_04_sign_in_without_registering(self):
        response = self.client.post("/api/v1/auth/sign_in", json={})
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("error", json_data)

    def test_05_sign_up_with_invalid_phone(self):
        response = self.client.post(
            "/api/v1/auth/sign_up", json=user_invalid_phone)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("error", json_data)

    def test_05_sign_up_with_short_password(self):
        response = self.client.post(
            "/api/v1/auth/sign_up", json=user_short_pass)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            json_data["error"],
            "password length should be between 6 to 16")

    def test_06_sign_up_without_data(self):
        response = self.client.post("/api/v1/auth/sign_up", json={})
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("error", json_data)

    def test_07_sign_up_with_correct_data(self):
        response = self.client.post("/api/v1/auth/sign_up", json=valid_user)
        json_data = json.loads(response.data)
        print(json_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(
            json_data["data"][0]["message"],
            "User registered")

    def test_08_sign_up_with_same_username_or_email(self):
        response = self.client.post("/api/v1/auth/sign_up", json=valid_user)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            json_data["error"],
            "username or email already exists")

    def test_09_sign_in_after_registering(self):
        response = self.client.post(
            "/api/v1/auth/sign_in", json=valid_sign_in)
        json_data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(json_data["data"][0]["message"], "User login")

    def test_10_sign_in_with_wrong_username(self):
        response = self.client.post(
            "/api/v1/auth/sign_in", json=sign_wrong_username)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(json_data["error"], "Username doesnt exist")

    def test_10_sign_in_with_wrong_password(self):
        response = self.client.post(
            "/api/v1/auth/sign_in", json=sign_wrong_password)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual(json_data["error"], "Enter correct password")

    def test_11_sign_up_with_wrong_data_type(self):
        response = self.client.post(
            "/api/v1/auth/sign_up", json=user_name_not_string)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("error", json_data)

    def test_12_sign_up_with_wrong_email(self):
        response = self.client.post(
            "/api/v1/auth/sign_up", json=user_invalid_email)
        json_data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertIn("error", json_data)
