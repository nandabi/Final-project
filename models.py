from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String)
    answer = Column(String)

    def __repr__(self):
        return f"<Question(id={self.id}, question='{self.question}', answer='{self.answer}')>"
