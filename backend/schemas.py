from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -----------------
# مسارات الإدارة (Admins)
# -----------------
class AdminBase(BaseModel):
        username: str
        full_name: str
        role: str = "admin"

class AdminCreate(AdminBase):
        password: str

class Admin(AdminBase):
        id: int

        class Config:
                from_attributes = True
                orm_mode = True

# -----------------
# مسارات المنتجات (Products)
# -----------------
class ProductBase(BaseModel):
        name: str
        category: str
        price: float
        image_url: Optional[str] = None
        is_available: bool = True

class ProductCreate(ProductBase):
        pass

class ProductPriceUpdate(BaseModel):
        price: float

class ProductAvailabilityUpdate(BaseModel):
        is_available: bool

class Product(ProductBase):
        id: int

        class Config:
                from_attributes = True
                orm_mode = True

# -----------------
# مسارات السجلات (Logs)
# -----------------
class LogEntryBase(BaseModel):
        action: str
        admin_id: Optional[int] = None

class LogEntry(LogEntryBase):
        id: int
        timestamp: datetime

        class Config:
                from_attributes = True
                orm_mode = True

# -----------------
# مسارات الطلبات (Orders) - (هذا القسم اللي جان مفقود)
# -----------------
class OrderBase(BaseModel):
        customer_name: str
        items: str
        total_price: float
        status: str = "قيد المعالجة"

class OrderCreate(OrderBase):
        pass

class OrderStatusUpdate(BaseModel):
        status: str

class Order(OrderBase):
        id: int

        class Config:
                from_attributes = True
                orm_mode = True