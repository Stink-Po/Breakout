from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# database + library://username:password@host:post/database
engine = create_engine("sqlite:///database.db")
base = declarative_base()
session = sessionmaker(bind=engine)()


class ScoresData(base):
    __tablename__ = "Score"
    id = Column("id", Integer, unique=True, primary_key=True)
    time = Column("time", Date)
    record = Column("record", Integer)

    def add(self, time, record):
        new_data = ScoresData(time=time, record=record)
        session.add(new_data)
        session.commit()


base.metadata.create_all(engine)

