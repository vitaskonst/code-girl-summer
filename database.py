# pip install databases sqlalchemy asyncpg psycopg2-binary
from databases import Database
from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    Identity,
    String,
    Text,
    DateTime,
    ARRAY,
    func
)

#  insert

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
# DATABASE_URL = "postgresql://codegirl:password@localhost:5432/database1"

database = Database(DATABASE_URL)
metadata = MetaData()

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("title", String),
    Column("content", Text),
    Column("author", String),
    Column("location", String),
    Column("image_urls", ARRAY(String)),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now())
)

# id - serial
# username - string
# password - string
# first_name - string
# last_name - string
# created_at - DateTime

users = Table(
    "users",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("username", String, unique=True),
    Column("password", String),
    Column("first_name", String),
    Column("last_name", String),
    Column("created_at", DateTime, server_default=func.now())
)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)
