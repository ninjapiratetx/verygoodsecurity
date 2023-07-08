from tkinter import W
from urllib import response
import requests
from src.static_values import API_CALL, BODY, HTTP_SUCCESS, HTTP_SUCCESS_POST, ID, NAME, TEST_USERID, URI, USERID 

POST_URI = f"{URI}{API_CALL}"

def get_all_posts():
    response = requests.get(POST_URI)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_last_post():
    json_of_results = get_all_posts()
    return json_of_results[len(json_of_results)-1]

def get_post_by_id(id):
    paramaters = {ID: id}
    return get_post_by_params(paramaters)

def get_post_by_params(paramaters):
    response = requests.get(POST_URI,params=paramaters)
    assert response.status_code == HTTP_SUCCESS
    return response.json()

def get_post_by_query_id(queryId):
    paramaters = {"userId":queryId}
    return get_post_by_params(paramaters)

def post_the_post(name,body,userId):
    post_json = {NAME:name, BODY:body, USERID:userId}
    response = requests.post(POST_URI,json=post_json)
    assert response.status_code == HTTP_SUCCESS_POST
    return response.json()

def compare_posts_to_each_query():
    json_of_results = get_all_posts()
    for res in json_of_results:
        id = res[ID]
        json_of_res = get_post_by_id(id)
        assert json_of_res == [res]

def compare_all_same_user_id_1():
    json_of_results = get_all_posts()
    json_of_query_1 = [res for res in json_of_results if res[USERID] == 1]
    json_of_query_from_call_1 = get_post_by_query_id(TEST_USERID) 
    assert json_of_query_from_call_1 == json_of_query_1