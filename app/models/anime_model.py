from . import conn_cur, commit_and_close


class Animes:
    def __init__():
        ...

    @staticmethod
    def create_db():
        conn, cur = conn_cur()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS animes (
                id BIGSERIAL PRIMARY KEY,
                anime VARCHAR(100) NOT NULL UNIQUE,
                released_date DATE NOT NULL,
                seasons INTEGER NOT NULL,
            )
        """)

        commit_and_close(conn,cur)
