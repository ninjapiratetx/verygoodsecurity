from src.request import compare_all_same_user_id_1, compare_posts_to_each_query

def test_get_post_by_id():
    compare_posts_to_each_query()

def test_get_post_by_queryId():
    compare_all_same_user_id_1()