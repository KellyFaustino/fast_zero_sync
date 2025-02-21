# from http import HTTPStatus

# from fastapi.testclient import TestClient

# from fast_zero import app

# client = TestClient(app)


# def test_read_root_return_ok_e_ola_mundo():
#     response = client.get('/')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Olá mundo!'}


from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_return_ok_e_ola_mundo():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Hello': 'Olá mundo!!'}
