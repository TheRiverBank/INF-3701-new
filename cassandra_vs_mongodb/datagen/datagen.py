###############################################################################
# Cast info | movie details | user reviews
#name, role | director, genera, runtime, release | timestamp comment
###############################################################################

GENRE = ["Action", "Comedy", "Romance"]
MIN_CAST = 1
MAX_CAST = 5

import json
from faker import Faker
import random

fake = Faker()



def create_movie():
    # General info
    movieId = fake.unique.random_int(0, 99999999999)
    movieName = fake.name()
    director = fake.name()
    writer = fake.name()
    genre = random.choice(GENRE)
    runtime = random.randint(60, 180)

    # Cast, nested
    castId = [fake.unique.random_int(0, 99999999999) for _ in range(MIN_CAST, MAX_CAST)]
    castName = [fake.name() for _ in range(MIN_CAST, MAX_CAST)]
    screenName = [fake.name() for _ in range(MIN_CAST, MAX_CAST)]
    payment = [random.randint(1000, 100000) for _ in range(MIN_CAST, MAX_CAST)]
    relatedMovies = [[fake.name() for _ in range(0, random.randint(0, 5))] for _ in range(MIN_CAST, MAX_CAST)]
    cast = []
    for i in range(0, MAX_CAST-MIN_CAST):
        cast.append(
            {
                "castId": castId[i],
                "screenName": screenName[i],
                "name": castName[i],
                "payment": payment[i],
                "relatedMovies": relatedMovies[i]
            }
        )

    movie = {
        "movieId": movieId,
        "movieName": movieName,
        "director": director,
        "writer": writer,
        "genre": genre,
        "runtime": runtime,
        "cast": cast
    }

    return movie


def generate_data_4_mongodb(N):
    """
    Creates "N" data samples and writes them to disk.
    The written data is compatible with MongoDB insertions
    """
    movies = []
    with open("movie.json", 'w') as f:
        for _ in range(N):
            movies.append(create_movie())
        f.write(json.dumps(movies))

def generate_data_4_cass_row():
    """
    Creates a data sample that is converted into
    a row that can be directly inserted into 
    Cassandra
    """

    movie = create_movie()
    data = list(movie.values())
    
    return data


if __name__ == "__main__":
    generate_data_4_cass_row()

