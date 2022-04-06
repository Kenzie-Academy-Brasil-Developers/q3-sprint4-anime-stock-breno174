from . import conn_cur, commit_and_close


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
    def serialize_data(payload):
        anime_columns = [
            'id',
            'anime',
            'released_date',
            'seasons'
        ]
        return dict(zip(anime_columns, payload))

    def one_anime(anime_id):
        conn, cur = conn_cur()

        query = 'SELECT * FROM animes WHERE id = %s'
        cur.execute(query, anime_id)
        animes = cur.fetchone()

        commit_and_close(conn, cur)
        return animes

