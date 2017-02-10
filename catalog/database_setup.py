import os

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


# User data
class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	email = Column(String(250), unique=True, nullable=False)
	name = Column(String(250), nullable=True)

# Item Categories
class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    cname = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
    	return {
    	    'id' : self.id,
    	    'name' : self.name,
    	}

# Items
class Item(Base):

    __tablename__ = 'item'

    iname = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
    	return {
    	    'id' : self.id,
    	    'name' : self.name,
    	    'description' : self.description,
    	    'category_id' : self.category_id,
    	}

# Engine
engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)

