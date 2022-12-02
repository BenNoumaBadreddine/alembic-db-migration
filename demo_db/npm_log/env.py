from logging.config import fileConfig
from urllib.parse import quote
import os
import sys
import inspect
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentdir)
currentdir = currentdir + '/db_bases'
sys.path.insert(0, currentdir)
from base import Base
target_metadata = Base.metadata



# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    try:
        # if a local db config is present use it in order to set the env variables. If not default to the regular env
        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parentdir = (os.path.dirname(currentdir))
        sys.path.insert(0, parentdir)
        import demo_db_config
        print(f'Configuration file demo_db_config (npm_log) is successfully imported.')
    except Exception:
        print(f'Configuration file demo_db_config (npm_log) NOT imported.')
        pass
    user = os.getenv("DB_USER", "ml_user")
    password = quote(os.getenv("USER_PASSWORD", "1234"))
    server = os.getenv("DB_SERVER", "localhost")
    db = os.getenv("DB_NAME", "")
    port = os.getenv("DB_PORT", "5432")
    return f"postgresql://{user}:{password}@{server}:{port}/{db}"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print(f'Starting online migration ...')
    configuration = config.get_section(config.config_ini_section)
    print(f'ini configuration {configuration}')
    configuration["sqlalchemy.url"] = get_url()
    print(f'After modification of ini configuration {configuration}')
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool, )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
