from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, autoincrement="auto", primary_key=True,  index=True)
    comment = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    
    usuario_dono = relationship("User", back_populates="comments")
    post_comentado = relationship("Post", back_populates="comments")
    