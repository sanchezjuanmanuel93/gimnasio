from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseDatos(object):

    def __init__(self):
        self.eng = create_engine('mysql+mysqlconnector://root:root@localhost/gimnasio')
        Session = sessionmaker(bind=self.eng)
        self.ses = Session()

    def getAll(self, query):
        return self.ses.query(query)

    def get_session(self):
        return self.ses
