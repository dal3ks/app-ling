from film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films')
        return [Film(row["id"], row["title"], row["genre"], row["release_date"]) for row in rows]
    
    def create(self,film):
        self._connection.execute('INSERT INTO films (title, genre, release_date) VALUES (%s, %s, %s)', [film.title, film.genre, film.release_date])
        return None