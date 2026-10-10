from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models
import schemas
from typing import List

# إنشاء الجداول في قاعدة البيانات (إذا ما موجودة)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# حل مشكلة الـ CORS حتى الواجهات (HTML) تكدر تتصل براحتها
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------
# التوجيه للصفحة الرئيسية
# -----------------
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


# -----------------
# مسارات الـ Admins
# -----------------

@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    if db_admin:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_admin = models.Admin(
        username=admin.username,
        hashed_password=admin.password, # للتجربة فقط، بالواقع لازم يتشفر
        full_name=admin.full_name,
        role=admin.role
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

@app.get("/admins/", response_model=List[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admins = db.query(models.Admin).offset(skip).limit(limit).all()
    return admins

@app.delete("/admins/{admin_id}")
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    db.delete(admin)
    db.commit()
    return {"detail": "Admin deleted successfully"}


# -----------------
# مسارات المنتجات (Products)
# -----------------

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.put("/products/{product_id}/price")
def update_price(product_id: int, price_update: schemas.ProductPriceUpdate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.price = price_update.price
    db.commit()
    return {"detail": "Price updated successfully"}

@app.put("/products/{product_id}/availability")
def update_availability(product_id: int, availability: schemas.ProductAvailabilityUpdate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.is_available = availability.is_available
    db.commit()
    return {"detail": "Availability updated successfully"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}


# -----------------
# مسارات السجلات (Logs)
# -----------------

@app.get("/logs/", response_model=List[schemas.LogEntry])
def read_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(models.LogEntry).order_by(models.LogEntry.timestamp.desc()).offset(skip).limit(limit).all()
    return logs