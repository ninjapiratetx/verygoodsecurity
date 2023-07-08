from src.request import get_last_post, post_the_post
from src.static_values import BODY, ID, NAME, TEST_BODY, TEST_NAME, TEST_USERID, USERID

def test_post_of_post():
    last_post_json_before = get_last_post()
    post_json = post_the_post(TEST_NAME,TEST_BODY,TEST_USERID)
    assert post_json[NAME] == TEST_NAME
    assert post_json[BODY] == TEST_BODY 
    assert post_json[USERID] == TEST_USERID
    assert post_json[ID] == last_post_json_before[ID]+1
    last_post_json_after = get_last_post()
    assert post_json == last_post_json_after 