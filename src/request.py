from urllib import response
import requests
from src.static_values import API_CALL, HTTP_SUCCESS, ID, URI 

POST_GET_URI = f"{URI}{API_CALL}"

def get_all_posts():
    response = requests.get(POST_GET_URI)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_last_post():
    json_of_results = get_all_posts()
    return json_of_results[len(json_of_results)-1]

def get_post_by_id(id):
    paramaters = {ID: id}
    return get_post_by_params(paramaters)

def get_post_by_params(paramaters):
    response = requests.get(f"{POST_GET_URI}",params=paramaters)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_post_by_query_id(queryId):
    paramaters = {"userId":queryId}
    return get_post_by_params(paramaters)

def compare_posts_to_each_query():
    json_of_results = get_all_posts()
    for res in json_of_results:
        id = res[ID]
        json_of_res = get_post_by_id(id)
        assert json_of_res == [res]

def compare_all_same_user_id_1():
    json_of_results = get_all_posts()
    json_of_query_1 = [res for res in json_of_results if res["userId"] == 1]
    json_of_query_from_call_1 = get_post_by_query_id(1) 
