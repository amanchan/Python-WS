
from fastapi import Header, APIRouter, HTTPException

from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api import db_manager
from app.api.service import is_cast_present

"""
fake_movie_db = [
    {
        'name' : 'Start Wars : Episode IX - The Rise of Skywalker',
        'plot' : 'The surviving members of theresistance face the First Order once again.',
        'generes': ['Action', 'Adventure', 'Fantacy'],
        'casts' : ['Daisy Ridley', 'Adam Driver']
    },
        {
        'name' : 'Dunki',
        'plot' : 'Illegal Immigration',
        'generes': ['Action', 'Comedy', 'Fantacy'],
        'casts' : ['Shah Rukh Khan', 'Tapsi Pannu', 'Boman Irani', 'Vicky Kaushal']
    }
]
"""

movies = APIRouter()

@movies.get('/', response_model=list[MovieOut])
async def index():
    return await db_manager.get_all_movies()

@movies.post('/', response_model=MovieOut, status_code=201)
async def add_movie(payload: MovieIn):
    for cast_id in payload.cast_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with id:{cast_id} not found")
    
    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }
    return response


@movies.get('/{id}', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset = True)
    movie_in_db = MovieIn(**movie)

    update_movie = movie_in_db.copy(update = update_data)
    return await db_manager.update_movie(id, updated_movie)

@movies.delete('/{id}')
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)

