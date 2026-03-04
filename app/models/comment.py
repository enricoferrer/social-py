from app.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, autoincrement="auto", primary_key=True,  index=True)
    comment = Column(String, nullable=False)
    commented_at = Column(DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    
    author = relationship("User", back_populates="comments")
    post_comentado = relationship("Post", back_populates="comments")
    