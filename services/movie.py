from __future__ import annotations

from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> List[Movie] | QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids
        ).all()

    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: int = None,
        actors_ids: int = None
) -> Movie:
    movie = Movie(
        title=movie_title,
        description=movie_description
    )
    movie.save()
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie