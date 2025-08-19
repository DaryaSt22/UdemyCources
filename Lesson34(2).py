user_profile = {
    'name': 'Daryshya',
    'comments_gty': 89,
}

def user_info(name, comments_gty = 0):  # В таком случае не может быть больше двух ключей в словаре
    if not comments_gty:
        return f"{name} has no comments"

    return f"{name} has {comments_gty} comments"

name, comments_gty = user_profile
print(name)
print(comments_gty)
print()

print(user_info(**user_profile))
print(user_info(user_profile))
print(user_info(user_profile['name'], user_profile['comments_gty']))
print(user_info(name=user_profile, comments_gty=user_profile))