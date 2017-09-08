from repositories import blog_repository

def page(page):
    blog = blog_repository.page(page)

    blog.posts = sorted(blog.posts, key=lambda p: p.date, reverse=True)

    return blog

