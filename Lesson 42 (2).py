class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()
darya = forum.register_user('daryshya', 'summer@gmail.com')
alice = forum.register_user('daya', 'sumr@gmail.com')
print(forum.users)

forum.create_post("My comment", "My first comment", darya)
print(forum.posts)
print(forum.posts[0].title)
print(forum.posts[0].content)
print(forum.posts[0].author.username)
print(forum.posts[0].author.email)

print(forum.find_user_by_username('daryshya'))

forum.create_post("Summer!", "Sunny", darya)
found_posts = forum.find_posts_by_author(darya)
print(found_posts)
print([post.title for post in found_posts])


user_email = 'summer@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User is email {user_email} doesn't exist!")
print(found_user)
