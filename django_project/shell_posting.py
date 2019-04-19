import json #to impost post.json
from blog.models import Post

# instance of opening and loading json data
with open('post.json') as f:
    posts_json = json.load(f)

# Loop through JSON data
for post in posts_json:
    """
    input:
        title: the title of the json element
        content: the cotent of the json element

        author_id: the user number of the json element, which is used as the
        ForeignKey to connect the blog site to the User database.
            Still trying to verify, but SQL convention is that the blog primary
            key would author and the foreign key should be author_id.

    output:
        After interation, it will post the JSON elements as new posts in blog
    """
    post = Post(title=post['title'],
    content=post['content'],
    author_id = post['user_id'])

    post.save()
