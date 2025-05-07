def sum_nums (*args):
    print(args)
    print(type(args))
    print(args[0])
    return sum(args)

print(sum_nums(2, 3, 7))

def get_posts_info(name, posts_gty):
    info = f"{name} wrote {posts_gty} posts"
    return info

info = get_posts_info('Daryshya',25)
print(info)