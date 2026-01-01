from database import engine
from models.users import Base

Base.metadata.create_all(bind=engine)
