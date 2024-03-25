from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from models import Base

# Import models here
from models import Question

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Ensure models are imported here so that they are registered with SQLAlchemy's metadata.
target_metadata = Base.metadata

# Below this line, add any custom renderers, filters, or operations you'd like to use in your migration scripts!

# Pass in the target metadata as a parameter to context.configure()
# This allows Alembic to compare the current state of the database to the model definitions.
# It also allows Alembic to generate migrations based on changes to the model definitions.
def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # When working with the database online, use the engine from the configuration.
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Bind the engine to the metadata of the Base class (which includes the models).
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    try:
        # Run migrations in the transaction.
        with context.begin_transaction():
            context.run_migrations()
    finally:
        # Close the connection.
        connection.close()

# If alembic is running offline (e.g., generating migrations),
# call the function to run migrations offline.
if context.is_offline_mode():
    run_migrations_offline()
else:
    # Otherwise, run migrations online (e.g., applying migrations to the database).
    run_migrations_online()
