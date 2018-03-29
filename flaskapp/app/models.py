from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CommonColumns(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())

class couverts(CommonColumns):
    __tablename__ = 'couverts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20))
    description = Column(String(150))
    in_stock = Column(Integer)
    price = Column(Float)
    orders = relationship("orders")

class orders(CommonColumns):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    couvert_id = Column(Integer, ForeignKey('couverts.id'), nullable=False)
    couvert = relationship("couverts", back_populates='orders')
    count = Column(Integer)

