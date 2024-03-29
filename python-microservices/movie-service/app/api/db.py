from sqlalchemy import (Column, Integer, MetaData, String, Table, 
                        create_engine, ARRAY)
from databases import Database
import os

#DATABASE_URI = 'postgresql://movie_user:movie_password@localhost/movie_db'
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('plot', String(250)),
    Column('generes', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

database = Database(DATABASE_URI)