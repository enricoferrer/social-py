from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.comment import Comment

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    usuario_dono = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post_comentado",cascade="all, delete")  