import sqlalchemy as db

class Db:

    def __init__(self, dialect:str, driver:str, user:str, password:str, host:str, port:(str or int), base_name:str) -> None:
        self._eng = db.create_engine(f'{dialect}+{driver}://{user}:{password}@{host}:{port}/{base_name}')

    def connect(self):
        try:
            return self._eng.connect()
        except:
            return False