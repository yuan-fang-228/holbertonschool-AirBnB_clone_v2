#!/usr/bin/python3
"""define a class to manage database storage"""
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
import os
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """define a class to manage database storage for hbnb project"""
    __engine = None
    __session = None

    def __init__(self):
        """initialise DBStorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        psd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        engeine = create_engine('mysql+mysqldb://{user}:{psd}@{host}/{db}',
                           pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test")
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """query on current database session all objects depending of class"""
        modelDict = {}
        classes = {User, State, City, Amenity, Place, Review}
        if cls is not None:
            classes = {cls}
        for cls in classes:
            objs = self.__session().query(cls).all()
            for obj in objs:
                key = cls.__name__ + "." + obj.id
                modelDict[key] = obj
        return modelDict

    def new(self, obj):
        """add object to current database"""
        self.__session().add(obj)

    def save(self):
        """commit all changes to current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and new database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
