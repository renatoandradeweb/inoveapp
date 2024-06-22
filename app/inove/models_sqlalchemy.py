from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)
    lat = Column(String)
    lng = Column(String)
    phone = Column(String)
    website = Column(String)
    company_name = Column(String)
    company_catch_phrase = Column(String)
    company_bs = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'address': {
                'street': self.street,
                'suite': self.suite,
                'city': self.city,
                'zipcode': self.zipcode,
                'geo': {
                    'lat': self.lat,
                    'lng': self.lng,
                }
            },
            'phone': self.phone,
            'website': self.website,
            'company': {
                'name': self.company_name,
                'catchPhrase': self.company_catch_phrase,
                'bs': self.company_bs,
            }
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'userId': self.user_id,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'deletedAt': self.deleted_at
        }
