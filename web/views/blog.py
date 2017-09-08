from flask import render_template, request
from app import app
from clients import page_client, blog_client
import base
from dateutil import parser

@app.route('/writings')
def blog():
    pageData = page_client.find('writings')
    if pageData == None or pageData.text == '{}':
        return render_template('404.html', nav=base.nav('/' + path))
    page = pageData.json()

    blog_page = request.args.get('page')
    if blog_page is None or blog_page < 0:
        blog_page = 0
    blogData = blog_client.paged(blog_page)
    if blogData == None or len(blogData.text) == 0 or blogData.text == '{}' or 'Not Found' in blogData.text:
        blog = {}
    else:
        blog = blogData.json()

    blog['archive'] = make_archive(blog)

    for post in blog['posts']:
        post['date'] = parser.parse(post['date']).strftime('%B %d, %Y')

    allow_newer = 'disabled'
    newer_class = 'secondary'
    if int(blog_page) > 0:
        allow_newer = ''
        newer_class = 'primary'

    allow_older = 'disabled'
    older_class = 'secondary'
    if len(blog['posts']) > 0:
        allow_older = ''
        older_class = 'primary'

    return render_template(page['template'], 
        nav=base.nav(page['path']), 
        blog_page=int(blog_page), 
        blog_allow_newer=allow_newer, 
        newer_class = newer_class,
        blog_allow_older=allow_older, 
        older_class=older_class,
        page=page, 
        blog=blog)


def make_archive(blog):
    dates = sorted(set([parser.parse(post['date']).strftime('%B %Y||%Y-%m') for post in blog['posts']]), reverse=True)
    return [{'name': d.split('||')[0], 'id': d.split('||')[1]} for d in dates]

