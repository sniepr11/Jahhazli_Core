from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float)
    img = Column(String)
    available = Column(Boolean, default=True)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    shop_name = Column(String)
    phone = Column(String)
    location = Column(String)
    items = Column(Text)
    total = Column(Float)
    date = Column(String)
    status = Column(String, default="جديد")

class ActivityLog(Base):
    __tablename__ = "activity_logs"
    id = Column(Integer, primary_key=True, index=True)
    admin_name = Column(String)
    action_type = Column(String)
    description = Column(String)
    date = Column(String)

# جدول حسابات الإدارة (الجديد)
class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    pin = Column(String)
    is_master = Column(Boolean, default=False)