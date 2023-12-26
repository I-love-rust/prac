import pytest
import allure
from faker import Faker
from jsondb import JsonServerBase

fake = Faker()

@pytest.fixture
def data():
    return {
            'user': {'id': 1, 'name': 'name'},
            'category': {'id': 1, 'name': 'name'},
            'post': {'id': 1, 'title': 'title', 'body': 'body', 'author_id': 1, 'category_id':1},
            'comment': {'id': 1, 'body': 'body', 'author_id': 1, 'post_id': 1},
            'some': {'id': 1, 'foo': 'bar'}
            }


############## USERS ##############
@allure.story("users")
@allure.title("create user")
def test_create_user(data):
    user = data['user']
    item, status = JsonServerBase.create('users', user)
    assert status == 201

@allure.story("users")
@allure.title("get all users")
def test_get_all_users(data):
    users, status = JsonServerBase.get_all('users')
    assert status == 200
    assert len(users) == 1
    assert users[0] == data['user']


@allure.story("users")
@allure.title("get user by id")
def test_get_user_by_id(data):
    user, status = JsonServerBase.get_one('users', data['user']['id'])
    assert status == 200
    assert user['id'] == data['user']['id']

@allure.story("users")
@allure.title("update user by id")
def test_update_user(data):
    new_user = data['user']
    new_user['name'] = fake.name()
    user, status = JsonServerBase.update('users', data['user']['id'], new_user)
    assert status == 200
    assert new_user == user

@allure.story("users")
@allure.title("delete user by id")
def test_delete_user(data):
    _, status = JsonServerBase.delete('users', data['user']['id'])
    assert status == 200
############## USERS ##############



############## CATEGORIES ##############
@allure.story("categories")
@allure.title("create category")
def test_create_category(data):
    category = data['category']
    item, status = JsonServerBase.create('categories', category)
    assert status == 201

@allure.story("categories")
@allure.title("get all categories")
def test_get_all_categories(data):
    categories, status = JsonServerBase.get_all('categories')
    assert status == 200
    assert len(categories) == 1
    assert categories[0] == data['category']

@allure.story("categories")
@allure.title("get category by id")
def test_get_category_by_id(data):
    category, status = JsonServerBase.get_one('categories', data['category']['id'])
    assert status == 200
    assert category['id'] == data['user']['id']

@allure.story("categories")
@allure.title("update category by id")
def test_update_category(data):
    new_category = data['category']
    new_category['name'] = fake.words()[0]
    category, status = JsonServerBase.update('categories', data['category']['id'], new_category)
    assert status == 200
    assert new_category == category

@allure.story("categories")
@allure.title("delete category by id")
def test_delete_category(data):
    _, status = JsonServerBase.delete('categories', data['category']['id'])
    assert status == 200
############## CATEGORIES ##############



############## POSTS ##############
@allure.story("posts")
@allure.title("create post")
def test_create_post(data):
    post = data['post']
    item, status = JsonServerBase.create('posts', post)
    assert status == 201

@allure.story("posts")
@allure.title("get all posts")
def test_get_all_posts(data):
    posts, status = JsonServerBase.get_all('posts')
    assert status == 200
    assert len(posts) == 1
    assert posts[0] == data['post']

@allure.story("posts")
@allure.title("get post by id")
def test_get_post_by_id(data):
    post, status = JsonServerBase.get_one('posts', data['post']['id'])
    assert status == 200
    assert post['id'] == data['post']['id']

@allure.story("posts")
@allure.title("update post by id")
def test_update_post(data):
    new_post = data['post']
    new_post['title'] = fake.words()[0]
    post, status = JsonServerBase.update('posts', data['post']['id'], new_post)
    assert status == 200
    assert new_post == post

@allure.story("posts")
@allure.title("delete post by id")
def test_delete_post(data):
    _, status = JsonServerBase.delete('posts', data['post']['id'])
    assert status == 200
############## POSTS ##############



############## COMMENTS ##############
@allure.story("comment")
@allure.title("create comment")
def test_create_comment(data):
    comment = data['comment']
    item, status = JsonServerBase.create('comments', comment)
    assert status == 201

@allure.story("comment")
@allure.title("get all comments")
def test_get_all_comments(data):
    comments, status = JsonServerBase.get_all('comments')
    assert status == 200
    assert len(comments) == 1
    assert comments[0] == data['comment']

@allure.story("comment")
@allure.title("get comment by id")
def test_get_comment_by_id(data):
    comment, status = JsonServerBase.get_one('comments', data['comment']['id'])
    assert status == 200
    assert comment['id'] == data['comment']['id']

@allure.story("comment")
@allure.title("update comment by id")
def test_update_comment(data):
    new_comment = data['comment']
    new_comment['body'] = fake.words()[0]
    comment, status = JsonServerBase.update('comments', data['comment']['id'], new_comment)
    assert status == 200
    assert new_comment == comment

@allure.story("comment")
@allure.title("delete comment by id")
def test_delete_comment(data):
    _, status = JsonServerBase.delete('comments', data['comment']['id'])
    assert status == 200
############## COMMENTS ##############



############## SOME ##############
@allure.story("some")
@allure.title("create some")
def test_create_some(data):
    some = data['some']
    item, status = JsonServerBase.create('some', some)
    assert status == 201

@allure.story("some")
@allure.title("get all some")
def test_get_all_some(data):
    some, status = JsonServerBase.get_all('some')
    assert status == 200
    assert len(some) == 1
    assert some[0] == data['some']

@allure.story("some")
@allure.title("get some by id")
def test_get_some_by_id(data):
    some, status = JsonServerBase.get_one('some', data['some']['id'])
    assert status == 200
    assert some['id'] == data['user']['id']

@allure.story("some")
@allure.title("update some by id")
def test_update_some(data):
    new_some = data['some']
    new_some['foo'] = fake.words()[0]
    some, status = JsonServerBase.update('some', data['some']['id'], new_some)
    assert status == 200
    assert new_some == some

@allure.story("some")
@allure.title("delete some by id")
def test_delete_some(data):
    _, status = JsonServerBase.delete('some', data['some']['id'])
    assert status == 200
