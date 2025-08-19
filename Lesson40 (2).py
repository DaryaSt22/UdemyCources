class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty

my_comment = Comment("My comment")

print(my_comment)
print(type(my_comment))
print(my_comment.__dict__)
print(dir(my_comment))
print(my_comment.text)
print(my_comment.votes_qty)

my_comment.upvote(5)
my_comment.upvote(5)
print(my_comment.votes_qty)
print()
my_comment.upvote = 10

second_comment = Comment("Second comment!")
second_comment.upvote(5)
print(second_comment.votes_qty)
