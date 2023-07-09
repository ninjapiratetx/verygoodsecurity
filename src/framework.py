from src.static_values import BODY, HTTP_SUCCESS, HTTP_SUCCESS_POST, ID, TITLE, POST_URI, USERID 
import requests

def get_all_posts() -> list:
    response = requests.get(POST_URI)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_last_post() -> dict:
    json_of_results = get_all_posts()
    return json_of_results[len(json_of_results)-1]

def get_post_by_id(id) -> list:
    paramaters = {ID: id}
    return get_post_by_params(paramaters)

def get_post_by_params(paramaters) -> list:
    response = requests.get(POST_URI,params=paramaters)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_post_by_query_id(queryId) -> list:
    paramaters = {"userId":queryId}
    return get_post_by_params(paramaters)

def post_the_post(name,body,userId) -> list:
    post_json = {TITLE:name, BODY:body, USERID:userId}
    response = requests.post(POST_URI,json=post_json)
    assert response.status_code == HTTP_SUCCESS_POST
    return response.json()

