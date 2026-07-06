"""
Casos de prueba de API usando la biblioteca Requests contra la API
publica JSONPlaceholder (no requiere autenticacion). Cubre GET, POST
y DELETE, valida codigos de estado y estructura/contenido de las
respuestas JSON, e incluye un escenario de encadenamiento de
peticiones (crear recurso y luego consultar el listado).
"""
import logging
import requests
import pytest

logger = logging.getLogger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post_returns_200_and_correct_structure():
    """GET /posts/{id} debe devolver 200 y el JSON debe tener los campos esperados."""
    logger.info("Iniciando test: GET post existente y validar estructura")
    response = requests.get(f"{BASE_URL}/posts/1")
    logger.info(f"Respuesta recibida: status={response.status_code}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body
    assert "userId" in body
    logger.info("Test finalizado OK: estructura del post valida")


def test_get_post_not_found_returns_404():
    """Escenario negativo: GET a un post fuera del rango existente (1-100) debe devolver 404."""
    logger.info("Iniciando test negativo: GET post inexistente")
    response = requests.get(f"{BASE_URL}/posts/99999")
    logger.info(f"Respuesta recibida: status={response.status_code}")

    assert response.status_code == 404
    logger.info("Test finalizado OK: 404 confirmado")


def test_post_create_post_returns_201():
    """POST /posts crea un recurso nuevo (simulado); valida 201 y los datos devueltos."""
    payload = {"title": "Proyecto Final QA", "body": "Automatizacion con Python", "userId": 1}
    logger.info(f"Iniciando test: POST nuevo post con payload={payload}")
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    logger.info(f"Respuesta recibida: status={response.status_code}")

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body
    logger.info(f"Test finalizado OK: post creado con id={body['id']}")


def test_delete_post_returns_200():
    """
    DELETE /posts/{id} debe devolver 200 con un objeto vacio.
    Nota: JSONPlaceholder simula el borrado, no persiste el cambio real.
    """
    logger.info("Iniciando test: DELETE de un post existente")
    response = requests.delete(f"{BASE_URL}/posts/1")
    logger.info(f"Respuesta recibida: status={response.status_code}")

    assert response.status_code == 200
    assert response.json() == {}
    logger.info("Test finalizado OK: post eliminado (simulado)")


def test_chained_requests_create_then_fetch_list():
    """
    Encadenamiento de peticiones: primero crea un post (POST) y
    luego valida que el listado general de posts (GET) siga
    respondiendo correctamente con datos consistentes.
    """
    logger.info("Iniciando test encadenado: crear post y luego listar")
    create_payload = {"title": "Nuevo Post", "body": "Contenido de prueba", "userId": 2}
    create_response = requests.post(f"{BASE_URL}/posts", json=create_payload)
    logger.info(f"Paso 1 (POST) -> status={create_response.status_code}")
    assert create_response.status_code == 201

    list_response = requests.get(f"{BASE_URL}/posts")
    logger.info(f"Paso 2 (GET listado) -> status={list_response.status_code}")
    assert list_response.status_code == 200
    body = list_response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    logger.info(f"Test finalizado OK: listado tiene {len(body)} posts")
