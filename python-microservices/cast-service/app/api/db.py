from sqlalchemy import (Column, Integer, MetaData, String, Table, 
                        create_engine)
from databases import Database
import os

#DATABASE_URI = 'postgresql://movie_user:movie_password@localhost/cast_db'
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('nationality', String(20)),

)

database = Database(DATABASE_URI)