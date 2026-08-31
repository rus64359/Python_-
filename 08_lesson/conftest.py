import os
import time
import pytest

from yougile_api import YouGileAPI

@pytest.fixture(scope="session")
def api():
    """Возвращает инициализированный API-клиент."""
    token = os.getenv("YOUGILE_TOKEN")
    if not token:
       pytest.fail(
            "Переменная окружения YOUGILE_TOKEN не задана. "
            "Установите её перед запуском: export YOUGILE_TOKEN=ваш_ключ"
        )
    return YouGileAPI(token)

@pytest.fixture
def temp_project(api):
    """
    Создаёт временный проект для теста и удаляет его после.
    Возвращает словарь с id и title созданного проекта.
    """
    unique_title = f"TestProject_{int(time.time() * 1000)}"
    response = api.create_project(title=unique_title)
    assert response.status_code == 201, (
       f"Не удалось создать проект: {response.status_code} {response.text}"
    )
    project = response.json()
    project_id = project["id"]

    yield {"id": project_id, "title": unique_title}

# Уборка: помечаем проект удалённым
    try:
       api.update_project(project_id, deleted=True)
    except Exception:
       pass
