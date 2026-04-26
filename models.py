from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class ParsedPage(Base):
    __tablename__ = "parsed_pages"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True, nullable=False)
    title = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    content_length = Column(Integer, nullable=True)
    parsed_at = Column(DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "description": self.description,
            "content_length": self.content_length,
            "parsed_at": self.parsed_at.isoformat() if self.parsed_at else None
        }