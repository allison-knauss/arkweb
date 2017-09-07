import imp
from migrate.versioning import api
import sqlalchemy
import os
import sys
from models.base import metadata
from repositories import base_repository

# create_all requires all models to be imported
# For now, just do that here
from models.page import Page


SQLALCHEMY_ENGINE_URI = os.environ['SQLALCHEMY_ENGINE_URI']
SQLALCHEMY_DATABASE = os.environ['SQLALCHEMY_DATABASE']
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_ENGINE_URI + '/' + SQLALCHEMY_DATABASE
SQLALCHEMY_MIGRATE_REPO = os.environ['SQLALCHEMY_MIGRATE_REPO']
SQLALCHEMY_TRACK_MODIFICATIONS = True

def createdb():
    try:
        with sqlalchemy.create_engine(SQLALCHEMY_ENGINE_URI, isolation_level='AUTOCOMMIT').connect() as connection:
            connection.execute('CREATE DATABASE ' + SQLALCHEMY_DATABASE)
    except:
        pass

def create():
    createdb()
    metadata.create_all(base_repository.engine)
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
    print('Created repository')

def migrate():
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    exec(old_model, tmp_module.__dict__)
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, metadata)
    open(migration, "wt").write(script)
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print('New migration saved as ' + migration)
    print('Current database version: ' + str(v))

def upgrade():
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print('Current database version: ' + str(v))

def downgrade():
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print('Current database version: ' + str(v))

if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == 'create':
        create()
    elif cmd == 'migrate':
        migrate()
    elif cmd == 'upgrade':
        upgrade()
    elif cmd == 'downgrade':
        downgrade()
    else:
        print('Unrecognized command: ' + cmd)
