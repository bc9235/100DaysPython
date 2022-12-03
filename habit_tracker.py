import requests
from datetime import date

USERNAME = "YOURUSERNAME"
TOKEN = "YOURPASSWORD"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADER = {
    "X-USER-TOKEN": TOKEN,
}


def create_user():
    """Create user account"""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(user_response.text)


def create_graph(graph_id):
    """Create user graph"""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

    graph_config = {
        "id": graph_id,
        "name": "Reading Graph",
        "unit": "pages",
        "type": "int",
        "color": "sora",
    }

    graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADER)
    print(graph_response.text)


def add_data(graph_id):
    """Add new data"""
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

    pages = int(input("How many pages did you read? "))

    if pages > 0:
        pixel_params = {
            "date": today,
            "quantity": str(pages),
        }

        pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HEADER)
        print(pixel_response.text)


def edit_data(graph_id):
    """Edit a pixel"""
    edit_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{today}"

    pages = int(input("How many pages did you read? "))

    if pages > 0:
        pixel_params = {
            "quantity": str(pages),
        }

        pixel_response = requests.put(url=edit_endpoint, json=pixel_params, headers=HEADER)
        print(pixel_response.text)


def delete_data(graph_id):
    """Delete a pixel"""
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{today}"

    pixel_response = requests.delete(url=delete_endpoint, headers=HEADER)
    print(pixel_response.text)


today = date.today().strftime("%Y%m%d")

graph = "YOURGRAPHNAME"

# create_user()
# create_graph(graph)
# add_data(graph)
# edit_data(graph)
# delete_data(graph)
