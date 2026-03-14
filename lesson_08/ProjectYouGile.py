import requests
from dotenv import load_dotenv
import os


class ProjectYouGile:

    def __init__(self, url) -> None:
        self.url = url
        load_dotenv()

    def create_new_project(self, title, user_id):
        url = f'{self.url}/projects'
        key = os.getenv("KEY")
        token = f'Bearer {key}'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        data = {
            'title': title,
            'users': {
                user_id: "admin"
            }
        }
        response = requests.post(url, headers=headers, json=data)
        status_code = response.status_code
        project = response.json()
        return status_code, project

    def change_new_project(self, id_project, new_title, user_id):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv("KEY")
        token = f'Bearer {key}'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        data = {
            'title': new_title,
            'users': {
                user_id: "admin"
            }
        }
        response = requests.put(url, headers=headers, json=data)
        status_code = response.status_code
        new_project = response.json()
        return status_code, new_project

    def get_new_project(self, id_project):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv("KEY")
        token = f'Bearer {key}'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        project_id = response.json()
        return status_code, project_id

    def delete_project(self, id_project):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv("KEY")
        token = f'Bearer {key}'
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        data = {
            "deleted": True
        }
        response = requests.put(url, headers=headers, json=data)
        status_code = response.status_code
        r = response.json()
        return status_code, r
