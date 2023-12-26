import requests
import logging

base_url = "http://localhost:3000/"

logging.basicConfig(filename="logs.log", level=logging.DEBUG)

class JsonServerBase:
    def get_all(entity) -> tuple[str, int]:
        response = requests.get(base_url + entity)
        logging.info(f"GET all {entity} - Status Code: {response.status_code}")
        return response.json(), response.status_code

    def get_one(entity, item_id) -> tuple[str, int]:
        response = requests.get(f"{base_url}{entity}/{item_id}")
        logging.info(f"GET {entity} with ID {item_id} - Status Code: {response.status_code}")
        return response.json(), response.status_code

    def create(entity, data) -> tuple[str, int]:
        response = requests.post(base_url + entity, json=data)
        logging.info(f"CREATE {entity} - Status Code: {response.status_code}")
        return response.json(), response.status_code

    def update(entity, item_id, data) -> tuple[str, int]:
        response = requests.put(f"{base_url}{entity}/{item_id}", json=data)
        logging.info(f"UPDATE {entity} with ID {item_id} - Status Code: {response.status_code}")
        return response.json(), response.status_code

    def delete(entity, item_id) -> tuple[str, int]:
        response = requests.delete(f"{base_url}{entity}/{item_id}")
        logging.info(f"DELETE {entity} with ID {item_id} - Status Code: {response.status_code}")
        return response.json(), response.status_code
