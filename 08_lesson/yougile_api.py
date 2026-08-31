import os
import requests

class YouGileAPI:
    """Page Object для работы с API YouGile (раздел Projects)."""

    BASE_URL = "https://ru.yougile.com/api-v2"

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError(
                "Не указан API-ключ. "
                "Установите переменную окружения YOUGILE_TOKEN "
                "или передайте token в конструктор."
            )
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )

 # ── POST /api-v2/projects ──────────────────────────────────

    def create_project(self, title: str, users: dict | None = None) -> requests.Response:
        """Создать проект. users — словарь {user_id: role}."""
        payload = {"title": title}
        if users is not None:
            payload["users"] = users
        return self.session.post(f"{self.BASE_URL}/projects", json=payload)

    def create_project_raw(self, payload: dict) -> requests.Response:
        """Создать проект с произвольным телом (для негативных тестов)."""
        return self.session.post(f"{self.BASE_URL}/projects", json=payload)

 # ── GET /api-v2/projects/{id} ──────────────────────────────

    def get_project(self, project_id: str) -> requests.Response:
        """Получить проект по ID."""
        return self.session.get(f"{self.BASE_URL}/projects/{project_id}")

    # ── PUT /api-v2/projects/{id} ───────────────────────────────

    def update_project(
        self,
        project_id: str,
        title: str | None = None,
        users: dict | None = None,
        deleted: bool | None = None,
    ) -> requests.Response:
        """Обновить проект: название, пользователей, пометить удалённым."""
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        if deleted is not None:
            payload["deleted"] = deleted
        return self.session.put(
            f"{self.BASE_URL}/projects/{project_id}", json=payload
        )

    def update_project_raw(
        self, project_id: str, payload: dict) -> requests.Response:
        """Обновить проект с произвольным телом (для негативных тестов)."""
        return self.session.put(
            f"{self.BASE_URL}/projects/{project_id}", json=payload
        )