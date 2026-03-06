from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int

    class Config:
        from_attributes = True

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    order_date: date

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int

    class Config:
        from_attributes = True