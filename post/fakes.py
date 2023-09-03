from faker import Faker

from post.models import Post

faker = Faker()

images = [
    "post/hello_ai_blog.png",
]


def insert_date_in_post(size=50):
    for i in range(size):
        post = Post.objects.create(
            title=faker.sentences(),
            content=faker.sentences(),
            author=faker.name(),
            image=images[0],
        )
