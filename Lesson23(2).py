def get_posts_info(**person):
    print(person)
    # info = f"{name} wrote {posts_gty} posts"
    print(type(person))
    info = (
        f"{person ['name']} wrote "
        f"{person ['posts_qty']} posts"
    )
    return info

info = get_posts_info(name='Darshylya', posts_qty=30, id=1351)
print(info)