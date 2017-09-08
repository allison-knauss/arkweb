from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
blog_posts = Table('blog_posts', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('date', DateTime),
    Column('content', String),
    Column('blog_id', Integer, ForeignKey("blogs.id")),
)

blogs = Table('blogs', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('description', String),
    Column('about', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['blogs'].create()
    post_meta.tables['blog_posts'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['blogs'].drop()
    post_meta.tables['blog_posts'].drop()
