# import create_engine

from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL='postgresql+psycopg2://neondb_owner:npg_8I6VlAbfQOYd@ep-royal-breeze-atn0r7dp-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
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