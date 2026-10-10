from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

# -----------------
# Admin Schemas
# -----------------
class AdminBase(BaseModel):
    username: str
    full_name: Optional[str] = None
    role: str

class AdminCreate(AdminBase):
    password: str

class Admin(AdminBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# -----------------
# Product Schemas
# -----------------
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ProductCreate(ProductBase):
    pass

class ProductPriceUpdate(BaseModel):
    price: float

class ProductAvailabilityUpdate(BaseModel):
    is_available: bool

class Product(ProductBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# -----------------
# Log Schemas
# -----------------
class LogEntryBase(BaseModel):
    action: str
    details: Optional[str] = None

class LogEntryCreate(LogEntryBase):
    pass

class LogEntry(LogEntryBase):
    id: int
    timestamp: datetime
    
    model_config = ConfigDict(from_attributes=True)