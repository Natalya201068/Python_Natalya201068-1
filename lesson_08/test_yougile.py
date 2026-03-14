import pytest
from dotenv import load_dotenv
import os
from ProjectYouGile import ProjectYouGile


load_dotenv()


@pytest.fixture(scope="session")
def api():
    url = "https://ru.yougile.com/api-v2"
    return ProjectYouGile(url)


@pytest.fixture
def temp_project(api):
    title = 'Test Project'
    user_id = os.getenv("USER_ID")
    status, project = api.create_new_project(title, user_id)
    assert status == 201, "Не удалось создать проект для теста"
    yield project
    api.delete_project(project["id"])


def test_create_new_project(api):
    title = 'Project2'
    user_id = os.getenv("USER_ID")
    status, project = api.create_new_project(title, user_id)
    assert status == 201
    assert project["id"] is not None
    status_code, response = api.delete_project(project["id"])
    assert status_code == 200
    status_code, response = api.get_new_project(project["id"])
    assert status_code == 200, f"Получили {status_code}"
    assert response["deleted"] is True


def test_create_new_project_negative(api):
    title = 'Project2'
    status, project = api.create_new_project(title, '12345')
    assert status == 400
    assert "Сотрудники со следующими ID не найдены в компании: 12345" in project.get("message")


def test_change_new_project(api, temp_project):
    new_title = 'Project3'
    user_id = os.getenv("USER_ID")
    status, new_project = api.change_new_project(temp_project['id'], new_title, user_id)
    assert status == 200
    assert new_project is not None
    api.delete_project(new_project["id"])


def test_change_new_project_negative(api):
    new_title = 'Project3'
    user_id = os.getenv("USER_ID")
    status, new_project = api.change_new_project('67890', new_title, user_id)
    assert status == 404
    assert "Проект не найден" in new_project.get("message")


def test_get_new_project(api, temp_project):
    status, project_data = api.get_new_project(temp_project['id'])
    assert status == 200
    assert project_data['id'] == temp_project['id']
    api.delete_project(project_data["id"])


def test_get_new_project_negative(api):
    status, project_id = api.get_new_project(api)
    assert status == 404
    assert 'Проект не найден' in project_id.get("message")
