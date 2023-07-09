from src.static_values import ID, BODY, SIZE_OF_USERID_1, TEST_USERID_NOT_IN_POSTS, TITLE, TEST_BODY_HARDCODED, TEST_ID, TEST_TITLE_HARDCODED, TEST_USERID, TITLE, USERID
from src.framework import get_all_posts, get_post_by_id, get_post_by_query_id

def test_get_post_by_id():
     json_of_res = get_post_by_id(TEST_ID)[0]
     assert json_of_res[ID] == TEST_ID
     assert json_of_res[TITLE] == TEST_TITLE_HARDCODED
     assert json_of_res[BODY] == TEST_BODY_HARDCODED
     assert json_of_res[USERID] == TEST_USERID
        
def test_get_all_post_by_id():
    json_of_results = get_all_posts()
    for res in json_of_results:
        id = res[ID]
        json_of_res = get_post_by_id(id)
        assert json_of_res == [res]

def test_get_post_by_queryId():
    json_of_query_from_call_1 = get_post_by_query_id(TEST_USERID) 
    assert len(json_of_query_from_call_1) == SIZE_OF_USERID_1

def test_get_post_query_id_not_in_list():
    json_of_query_from_call_1 = get_post_by_query_id(TEST_USERID_NOT_IN_POSTS) 
    assert len(json_of_query_from_call_1) == 0 
    
def test_get_all_post_by_queryId():
    json_of_results = get_all_posts()
    json_of_query_1 = [res for res in json_of_results if res[USERID] == 1]
    json_of_query_from_call_1 = get_post_by_query_id(TEST_USERID) 
    assert json_of_query_from_call_1 == json_of_query_1