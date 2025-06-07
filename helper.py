import allure
import requests

from urls import TestUrl


class UserMethods:

    @allure.step('создать нового пользователя')
    def create_user(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
            }

        response = requests.post(TestUrl.CREATE_USER, json=payload)

        return {
            "email": payload.get("email"),
            "password": payload.get("password"),
            "name": payload.get("name"),
            "response": response
        }

    @allure.step('удалить пользователя')
    def delete_user(self, token):
        clean_token = token.replace("Bearer ", "") if token else token

        headers = {
            "Authorization": f"Bearer {clean_token}",  # Добавляем Bearer здесь
            "Content-Type": "application/json"
        }
        response = requests.delete(TestUrl.DELETE_USER, headers=headers)
        return response