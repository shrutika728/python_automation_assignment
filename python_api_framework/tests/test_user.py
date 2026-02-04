import pytest
from services.user_services import UserService
from tests.test_data import user_data

@pytest.fixture
def mock_session():
    class Resp:
        def __init__(self, json_data, status_code):
            self._json = json_data
            self.status_code = status_code

        def json(self):
            return self._json

    class MockSession:
        def get(self, url, params=None, timeout=None):
            if url.endswith("/users") and params and params.get("page") == 2:
                return Resp({"data": [{"id": 1}, {"id": 2}]}, 200)
            if url.endswith("/users/2"):
                return Resp({"data": {"id": 2, "first_name": "Janet"}}, 200)
            return Resp(None, 404)

        def post(self, url, json=None, timeout=None):
            payload = json or {}
            created = {"name": payload.get("name")}
            if "job" in payload:
                created["job"] = payload.get("job")
            created.update({"id": "123", "createdAt": "2026-02-04T00:00:00.000Z"})
            return Resp(created, 201)

    return MockSession()

@pytest.fixture
def user_service(mock_session):
    return UserService(session=mock_session)

def test_get_users(user_service):
    response, status_code = user_service.get_users(page=2)
    assert status_code == 200
    assert "data" in response
    assert isinstance(response["data"], list)

@pytest.mark.parametrize("payload", user_data)
def test_create_user(user_service, payload):
    response, status_code = user_service.create_user(payload=payload)
    assert status_code == 201
    assert response["name"] == payload["name"]
    assert response["job"] == payload["job"]

def test_get_single_user(user_service):
    user_id = 2
    response, status_code = user_service.get_user(user_id=user_id)
    assert status_code == 200
    assert "data" in response
    assert response["data"]["id"] == user_id

def test_get_user_not_found(user_service):
    user_id = 23
    response, status_code = user_service.get_user(user_id=user_id)
    assert status_code == 404
    assert response == {}

def test_create_user_missing_fields(user_service):
    payload = {"name": "John"}
    response, status_code = user_service.create_user(payload=payload)
    assert status_code == 201
    assert response["name"] == payload["name"]
    assert "job" not in response

def test_get_users_count(user_service):
    response, status_code = user_service.get_users(page=2)
    assert status_code == 200
    assert len(response["data"]) == 2

def test_create_user_includes_metadata(user_service):
    payload = {"name": "Eve", "job": "Tester"}
    response, status_code = user_service.create_user(payload=payload)
    assert status_code == 201
    assert "id" in response
    assert "createdAt" in response

def test_create_user_bad_request_returns_400():
    class Resp:
        def __init__(self, status_code):
            self.status_code = status_code

        def json(self):
            raise ValueError("no json")

    class BadSession:
        def post(self, url, json=None, timeout=None):
            return Resp(400)

        def get(self, url, params=None, timeout=None):
            return Resp(400)

    svc = UserService(session=BadSession())
    response, status_code = svc.create_user(payload={})
    assert status_code == 400
    assert response == {}

def test_get_users_empty_page_returns_404(user_service):
    response, status_code = user_service.get_users(page=99)
    assert status_code == 404
    assert response == {}