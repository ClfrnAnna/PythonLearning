import pytest
from fastapi import status


class TestTasks:
    api = "/api/tasks"

    @pytest.fixture
    def body(self):
        return {
            "status": "UNCHECKED",
            "difficulty_level": 4,
            "student_id": 1,
            "lesson_id": 1,
        }

    def test_receiving_all_tasks(self, client):v
        response = client.get(self.api)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["tasks"]) > 0

    def test_creating_task(self, client, body):
        response = client.post(self.api, json=body)
        assert response.status_code == status.HTTP_201_CREATED

    def test_creating_task_with_invalid_body(self, client):
        response = client.post(self.api, json={"test": 1})
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_success_receiving_one_task(self, client):
        response = client.get(f"{self.api}/5")
        assert response.status_code == status.HTTP_200_OK

    def test_failure_receiving_one_task(self, client):
        response = client.get(f"{self.api}/150")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_success_edition_task(self, client):
        response = client.patch(f"{self.api}/6", json={"status": "SOLVED"})
        assert response.status_code == status.HTTP_200_OK

    def test_failure_editing_task(self, client):
        response = client.patch(f"{self.api}/150", json={"status": "SOLVED"})
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_deleting_task(self, client):
        response = client.delete(f"{self.api}/1")
        assert response.status_code == status.HTTP_204_NO_CONTENT
