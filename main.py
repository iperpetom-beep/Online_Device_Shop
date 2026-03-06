from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from bd import models, schemas, crud, database
from typing import List

app = FastAPI(title="Онлайн-магазин електроніки")

database.create_tables()

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.get("/customers/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@app.get("/sales/total")
def get_total_sales(db: Session = Depends(database.get_db)):
    return {"total_sales": crud.get_total_sales(db)}

@app.get("/customers/orders")
def get_orders_per_customer(db: Session = Depends(database.get_db)):
    results = crud.get_orders_per_customer(db)
    return [{"first_name": r[0], "last_name": r[1], "order_count": r[2]} for r in results]

@app.get("/orders/average")
def get_average_order_value(db: Session = Depends(database.get_db)):
    return {"average_order_value": crud.get_average_order_value(db)}

@app.get("/categories/popular")
def get_most_popular_category(db: Session = Depends(database.get_db)):
    result = crud.get_most_popular_category(db)
    if result:
        return {"category": result[0], "order_count": result[1]}
    return {"message": "No orders found"}

@app.get("/categories/products")
def get_products_per_category(db: Session = Depends(database.get_db)):
    results = crud.get_products_per_category(db)
    return [{"category": r[0], "product_count": r[1]} for r in results]

@app.put("/products/update_smartphones")
def update_smartphone_prices(db: Session = Depends(database.get_db)):
    crud.update_smartphone_prices(db)
    return {"message": "Smartphone prices updated by 10%"}