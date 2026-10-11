from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# مسار قاعدة البيانات (راح تنخزن بملف jahhazli.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./jahhazli.db"

# محرك الاتصال
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# جلسة الاتصال
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# الأساس اللي راح نبني عليه الجداول
Base = declarative_base()