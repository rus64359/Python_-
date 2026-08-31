"""
Автотесты для YouGile API v2 — методы работы с проектами.

POST /api-v2/projects        — создание проекта
PUT  /api-v2/projects/{id}   — обновление проекта
GET  /api-v2/projects/{id}   — получение проекта

Запуск:  pytest  (из папки 08_lesson)
Необходимо:  export YOUGILE_TOKEN=ваш_API_ключ
"""

import time

# ──────────────────────────────────────────────────────────────
# POST /api-v2/projects — создание проекта
# ──────────────────────────────────────────────────────────────

class TestCreateProject:
    """Тесты метода POST /api-v2/projects."""

    def test_create_project_positive(self, api):
        """Позитивный: создаём проект с корректным title."""
        title = f"APITest_Create_{int(time.time() * 1000)}"
        response = api.create_project(title=title)

        assert response.status_code == 201, (
             f"Ожидался 201, получен {response.status_code}: {response.text}"
        )
        body = response.json()
        assert body["title"] == title, "Название не совпадает"
        assert "id" in body, "В ответе нет id проекта"

 # Уборка
        api.update_project(body["id"], deleted=True)

    def test_create_project_negative_no_title(self, api):
        """Негативный: создаём проект без обязательного поля title."""
        response = api.create_project_raw({})
        (f"Ожидался 400/422, получен {response.status_code}: {response.text}"
        )

    def test_create_project_negative_empty_title(self, api):
        """Негативный: создаём проект с пустым title."""
        response = api.create_project(title="")

        assert response.status_code in (400, 422), (
            f"Ожидался 400/422, получен {response.status_code}: {response.text}"
        )

# ──────────────────────────────────────────────────────────────
# GET /api-v2/projects/{id} — получение проекта
# ──────────────────────────────────────────────────────────────

class TestGetProject:
    """Тесты метода GET /api-v2/projects/{id}."""

    def test_get_project_positive(self, api, temp_project):
        """Позитивный: получаем существующий проект по ID."""
        project_id = temp_project["id"]
        response = api.get_project(project_id)

        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}: {response.text}"
        )
        body = response.json()
        assert body["id"] == project_id, "ID не совпадает"
        assert body["title"] == temp_project["title"], "Title не совпадает"

    def test_get_project_negative_not_found(self, api):
        """Негативный: запрашиваем несуществующий проект."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.get_project(fake_id)

        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}: {response.text}"
        )

    def test_get_project_negative_invalid_id(self, api):
        """Негативный: передаём невалидный ID."""
        response = api.get_project("not-a-valid-uuid")

        assert response.status_code in (400, 404), (
            f"Ожидался 400/404, получен {response.status_code}: {response.text}"
        )

# ──────────────────────────────────────────────────────────────
# PUT /api-v2/projects/{id} — обновление проекта
# ──────────────────────────────────────────────────────────────

class TestUpdateProject:
    """Тесты метода PUT /api-v2/projects/{id}."""

    def test_update_project_positive(self, api, temp_project):
        """Позитивный: меняем название у существующего проекта."""
        project_id = temp_project["id"]
        new_title = f"Updated_{int(time.time() * 1000)}"

        response = api.update_project(project_id, title=new_title)

        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}: {response.text}"
        )
        body = response.json()
        assert body["title"] == new_title, "Название не обновилось"

    def test_update_project_positive_delete_flag(self, api, temp_project):
        """Позитивный: помечаем проект удалённым через флаг deleted."""
        project_id = temp_project["id"]

        response = api.update_project(project_id, deleted=True)

        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}: {response.text}"
        )

 # Проверяем, что проект действительно помечен удалённым
        get_response = api.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json().get("deleted") is True, (
            "Флаг deleted не установлен"
        )

    def test_update_project_negative_not_found(self, api):
        """Негативный: обновляем несуществующий проект."""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = api.update_project(fake_id, title="No Such Project")

        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}: {response.text}"
        )

    def test_update_project_negative_empty_title(self, api, temp_project):
        """Негативный: передаём пустой title при обновлении."""
        project_id = temp_project["id"]

        response = api.update_project(project_id, title="")

        assert response.status_code in (400, 422), (
            f"Ожидался 400/422, получен {response.status_code}: {response.text}"
        )