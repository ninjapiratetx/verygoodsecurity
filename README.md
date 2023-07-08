# verygoodsecurity
this is the code for the Very Good Security code exercise.  Which is to implement a get request posts with query id and post request post.  Load testing is in a seperate project:

# how to run
from directory verygoodsecurity
pip install -r requirements.txt
pytest

# the tests
For a get request with query id there two, first id:
For this test we compare each of the posts returned in a call to get all posts.  We then compare the posts using id to the call with the query parameter id.
steps:
1) Get all posts (expected results: all the posts, returns a status code of 200)
2) Loop throught all above posts (expected results: each above posts)
3) get id of current post (expected results: the id of the current post )
4) call get request with same request with parmas with id add (expected results: the post that matches the id)
5) compare current post to post returned in 4. (expected results: they match)

next user Id:
For this test we compare that for a given userid we match the results when we do a get posts with userid = 1.
steps:
1) Get all posts (expected results: all the posts, returns a status code of 200)
2) Loop throught all above posts (expected results: each above posts)
3) sort out all the results where userId == 1 (expected results: a list of posts with  userId == 1)
4) call the get request with the same request with parama with userId = 1 (expected results: a list of post with userId == 1)
5) compare the list 3 to 4 (expected results: they match)

next the post
For this test we do a post with a test body,  Verify the post sent the right things, then compare it to the last one in the list since the post added to it.  This is failing due to the list not updating with the value from the post.  This may or may not be a bug due to the way the setup is.  The post is not being added.  This is an issue which I would then discuss with the developers
steps:
1) get the last post in posts (expected results: a post that is the last post on the list)
2) post to the server with name = test, body = test test, userId = 1 (expected results: a post call with name,body,userId and id)
3) compare the result in 2 with name = test, body = test test userId =1 and id = the post id in step 1 + 1(expected results: they all match)
4) get the last post in posts (expected results: a post this is the last post on the list)
5) compare the results in step 2 to the results in step 4 (expected results: they match) (currently step 1 matches step 4, it appears not to be added to the list.  This may or may not be a bug)