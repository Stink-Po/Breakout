from datetime import datetime as dt
from sqlalchemy.orm import sessionmaker
import database

# Sizes

paddle_place = (0, -270)
ball_place = (0, -248)
score_place = (-400, 250)
width, height = 1000, 600
# colors

colors = ["dark green", "dark goldenrod", "peach puff", "orange red", "black"]

# font

font = ("Arial", 22, "bold")

# date

today = dt.now()

# database

data = database.ScoresData
session = sessionmaker(bind=database.engine)()
score_data = session.query(data).filter_by(id=1).first()
