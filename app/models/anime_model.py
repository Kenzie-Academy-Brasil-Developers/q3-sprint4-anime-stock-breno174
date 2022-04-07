from app.services.user_service import cash_keys
from . import conn_cur, commit_and_close
from psycopg2 import sql


class Animes:
    def __init__(self, anime: str, released_date: str, seasons: int):
        self.anime = anime.lower().title()
        self.released_date = released_date
        self.seasons = seasons

    @staticmethod
    def create_db():
        conn, cur = conn_cur()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS animes (
                id BIGSERIAL PRIMARY KEY,
                anime VARCHAR(100) NOT NULL UNIQUE,
                released_date DATE NOT NULL,
                seasons INTEGER NOT NULL
            );
        """)

        commit_and_close(conn, cur)

    def create_anime(self):
        conn, cur = conn_cur()

        data_anime = (self.anime, self.released_date, self.seasons)
        query = """
            INSERT INTO animes (anime, released_date, seasons)
            VALUES (%s, %s, %s)
            RETURNING *
        """

        cur.execute(query, data_anime)
        response = cur.fetchone()

        commit_and_close(conn, cur)

        return response

    @staticmethod
    def all_animes():
        conn, cur = conn_cur()
        query = 'SELECT * FROM animes'
        cur.execute(query)
        all_animes = cur.fetchall()

        commit_and_close(conn, cur)
        return all_animes

    @staticmethod
    def serialize_data(payload: dict):
        anime_columns = [
            'id',
            'anime',
            'released_date',
            'seasons'
        ]
        return dict(zip(anime_columns, payload))

    def one_anime(anime_id: str):
        conn, cur = conn_cur()

        query = 'SELECT * FROM animes WHERE id = %s'
        cur.execute(query, anime_id)
        animes = cur.fetchone()

        commit_and_close(conn, cur)
        return animes

    @staticmethod
    def dell_anime(anime_id: str):
        conn, cur = conn_cur()

        query = 'DELETE FROM animes WHERE id = %s RETURNING *'
        cur.execute(query, anime_id)
        animes = cur.fetchone()

        commit_and_close(conn, cur)
        return animes

    @staticmethod
    def update_anime(anime_id: str, payload: dict):
        conn, cur = conn_cur()

        payload = cash_keys(payload)

        colums = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        sql_anime_id = sql.Literal(anime_id)
        
        query = sql.SQL("""
            UPDATE animes SET ({colums}) = ROW ({values})  WHERE id = {id} RETURNING *
        """).format(
            id=sql_anime_id, 
            colums=sql.SQL(",").join(colums),
            values=sql.SQL(",").join(values),
        )
        cur.execute(query)
        update = cur.fetchone()

        commit_and_close(conn, cur)
        return update
