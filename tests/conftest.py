import pytest

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED",   "date": "2024-01-15T10:00:00"},
        {"id": 2, "state": "CANCELED",   "date": "2024-02-10T12:30:00"},
        {"id": 3, "state": "EXECUTED",   "date": "2024-03-11T14:15:00"},
        {"id": 4, "state": "PENDING",    "date": "2024-03-11T14:15:00"},
    ]


@pytest.fixture
def empty_list():
    return []