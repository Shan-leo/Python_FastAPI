from sqlalchemy import Column, Integer, String, Boolean
from .databse import Base


class Post(Base):
    __tablename = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
