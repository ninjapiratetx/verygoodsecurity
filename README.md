# verygoodsecurity
this is the code for the Very Good Security code exercise.  Which is to implement a get request posts with query id and post request post of https://jsonplaceholder.typicode.com/.  Load testing is in a seperate project: verygoodsecurityload

# how to run
from directory verygoodsecurity
pip install -r requirements.txt
pytest

# the tests
test_get_post_by_id
For this test we are comparing the first id against the call get posts by parameter id
steps:
1) call get request with params id = 1 (expected results - a record that matches param 1)
2) compare the title, body, id and userId with the hardcoded values (expected results - they all match the hardcode values)

test_get_all_post_by_id
For this test we compare each of the posts returned in a call to get all posts.  We then compare the posts using id to the call with the query parameter id.
steps:
1) get all posts (expected results: all the posts, returns a status code of 200)
2) Loop throught all above posts (expected results: each above posts)
3) get id of current post (expected results: the id of the current post )
4) call get request with same request with parmas with id add (expected results: the post that matches the id)
5) compare current post to post returned in 4. (expected results: they match)

test_get_post_by_queryId
for this test we are validate the request with params userId = 1 returns 10
steps:
1) call get requwst wirh params userId = 1 (expected result: a list of records that match userId)
2) compare the size of the list in 1 with 10 (expected result: The size is 10)

test_get_post_by_queryId
for this test we are validate the request with params userId = 1 returns 10
steps:
1) call get requwst wirh params userId = 11 (expected result: a list of records that match userId)
2) compare the size of the list in 1 with 10 (expected result: The size is 0)

test_post_added:
For this test we compare that for a given userid we match the results when we do a get posts with userid = 1.
steps:
1) get all posts (expected results: all the posts, returns a status code of 200)
2) loop throught all above posts (expected results: each above posts)
3) sort out all the results where userId == 1 (expected results: a list of posts with  userId == 1)
4) call the get request with the same request with parama with userId = 1 (expected results: a list of post with userId == 1)
5) compare the list 3 to 4 (expected results: they match)

test_post_of_post:
For this test verify the post sent the a result that match the name, body, and userId.
steps:
1) get the last post in posts (expected results: a post that is the last post on the list)
2) post to the server with title = test, body = test test, userId = 1 (expected results: a post call with name,body,userId and id)
3) compare the result in 2 with name = test, body = test test userId =1 and id = the post id in step 1 + 1(expected results: they all match)

test_post_added
For this test we are testing that user id that not get posts.
steps:
1) get the last post in posts (expected results: a post that is the last post on the list)
2) post to the server with title = test, body = test test, userId = 11 (expected results: a post call with name,body,userId and id)
3) compare the result in 2 with name = test, body = test test userId =1 and id = the post id in step 1 + 1(expected results: they all match)

test_post_added
For this test we do a post with a test values, then compares them to the last one add to the list which should match.   This is failing due to the list not updating with the value from the post.  This may or may not be a bug due to the way the setup is.  The post is not being added.  This is an issue which I would then discuss with the developers
steps:
1) post to the server with title = test, body = test test, userId = 1 (expected results: a post call with name,body,userId and id)
2) get the last post in posts (expected results: a post this is the last post on the list)
3) compare the results in step 2 to the results in step 4 (expected results: they match) (currently step 1 matches step 4, it appears not to be added to the list.  This may or may not be a bug)

# the screenshots of the results
![Alt text](/img/functionalTests.png?raw=true "All the functional tests")