import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    height = Column(String(120), unique=True, nullable=False)
    mass = Column(String(120), unique=True, nullable=False)
    hair_color = Column(String(120), unique=True, nullable=False)
    skin_color = Column(String(120), unique=True, nullable=False)
    eye_color = Column(String(120), unique=True, nullable=False)
    birth_year = Column(String(120), unique=True, nullable=False)
    gender = Column(String(120), unique=True, nullable=False)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    Base = Column(String(120), unique=True, nullable=False)
    manufacturer = Column(String(120), unique=True, nullable=False)
    cost_in_credits = Column(Integer, primary_key=True)
    length = Column(Integer, primary_key=True)
    max_atmosphering_speed = Column(Integer, primary_key=True)
    crew = Column(String(120), unique=True, nullable=False)
    passengers = Column(String(120), unique=True, nullable=False)
    cargo_capacity = Column(Integer, primary_key=True)
    vehicle_class = Column(String(120), unique=True, nullable=False)

class Starships(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    Base = Column(String(120), unique=True, nullable=False)
    manufacturer = Column(String(120), unique=True, nullable=False)
    cost_in_credits = Column(Integer, primary_key=True)
    length = Column(Integer, primary_key=True)
    max_atmosphering_speed = Column(Integer, primary_key=True)
    passengers = Column(String(120), unique=True, nullable=False)
    cargo_capacity = Column(Integer, primary_key=True)
    consumables = Column(String(120), unique=True, nullable=False)
    hyperdrive_rating = Column(Integer, primary_key=True)
    starship_class = Column(String(120), unique=True, nullable=False)

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    population = Column(Integer, unique=True, nullable=False)
    terrain = Column(String(120), unique=True, nullable=False)
    climate = Column(String(120), unique=True, nullable=False)
    diameter = Column(Integer, unique=True, nullable=False)
    gravity = Column(String(120), unique=True, nullable=False)
    users = relationship("Favorite", back_populates="user")

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False)
    planet_id = Column(ForeignKey('planet.id'), nullable=True)
    character_id = Column(ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(ForeignKey('vehicle.id'), nullable=True)
    user = relationship("Planet", back_populates="users")
    planet = relationship("User", back_populates="favorite_planets")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')