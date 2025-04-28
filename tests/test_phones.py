import pytest


def test_create_phone(client):
    response = client.post(
        "/write_data", json={"phone": "82934567890", "address": "Test Address"}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Data created successfully"}


def test_update_phone(client):
    client.post("/write_data", json={"phone": "82934567890", "address": "Old Address"})

    response = client.post(
        "/write_data", json={"phone": "82934567890", "address": "New Address"}
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Data updated successfully"}


def test_get_phone_existing(client):
    client.post("/write_data", json={"phone": "82934567890", "address": "Test Address"})
    response = client.get("/check_data", params={"phone": "82934567890"})
    assert response.status_code == 200
    assert response.json() == {"phone": "82934567890", "address": "Test Address"}


def test_get_phone_non_existing(client):
    response = client.get("/check_data/0000000000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
