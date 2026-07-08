# import create_engine

from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.ext.declarative import declarative_base

import os

from dotenv import load_dotenv
load_dotenv()
# import the function that can read a .rnv file , i.e open the .env file , and load all of its variables
# into the memory

DATABASE_URL= os.getenv("DATABASE_URL")
# here , we are connecting to a PostgreSQL database hosted on th cloud(Neon)

# note : click "show password" and copy th complete connection string

# create SQLAlchemy engine
# the engine is resposible for connecting FASTapi with the cloud PostgreSQL database
engine = create_engine(DATABASE_URL)

# create sessions as every database operation will use this session
SessionLocal = sessionmaker(bind = engine)

# base class as all database table will inherit from this  class
Base = declarative_base()

# dependency injection  , this function provides  a  session whenever an API requires database access
def get_db():
    db = SessionLocal()
    
    try:
        
        yield db
        
        
    finally:
        
        db.close()