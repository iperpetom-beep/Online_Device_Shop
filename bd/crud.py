from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def get_total_sales(db: Session):
    result = db.query(func.sum(models.Product.price * models.Order.quantity)).join(models.Order).scalar()
    return result or 0

def get_orders_per_customer(db: Session):
    results = db.query(
        models.Customer.first_name,
        models.Customer.last_name,
        func.count(models.Order.order_id).label("order_count")
    ).join(models.Order).group_by(models.Customer.customer_id).all()
    return results

def get_average_order_value(db: Session):
    result = db.query(func.avg(models.Product.price * models.Order.quantity)).join(models.Order).scalar()
    return result or 0

def get_most_popular_category(db: Session):
    result = db.query(
        models.Product.category,
        func.count(models.Order.order_id).label("order_count")
    ).join(models.Order).group_by(models.Product.category).order_by(func.count(models.Order.order_id).desc()).first()
    return result

def get_products_per_category(db: Session):
    results = db.query(
        models.Product.category,
        func.count(models.Product.product_id).label("product_count")
    ).group_by(models.Product.category).all()
    return results

def update_smartphone_prices(db: Session):
    db.query(models.Product).filter(models.Product.category == "смартфони").update({"price": models.Product.price * 1.1})
    db.commit()