
from src.static_values import BODY, ID, TITLE, TEST_BODY, TEST_TITLE, TEST_USERID, USERID
from src.framework import get_last_post, post_the_post

def test_post_of_post():
    last_post_json_before = get_last_post()
    post_json = post_the_post(TEST_TITLE, TEST_BODY,TEST_USERID)
    assert post_json[TITLE] == TEST_TITLE
    assert post_json[BODY] == TEST_BODY 
    assert post_json[USERID] == TEST_USERID
    assert post_json[ID] == last_post_json_before[ID]+1

def test_post_added():
    post_json = post_the_post(TEST_TITLE,TEST_BODY,TEST_USERID)
    last_post_json_after = get_last_post()
    assert post_json == last_post_json_after 