from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    username: str = Field(index=True)
    password: str
    role: str

    orders: List["OrderPurchase"] = Relationship(back_populates="user")

class Product(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str
    price: float
    quantity: int

    order_associations: List["OrderProductLink"] = Relationship(back_populates="product")

class OrderProductLink(SQLModel, table=True):
    id : Optional[int] = Field(primary_key=True)
    order_id: Optional[int] = Field(foreign_key="orderpurchase.id", primary_key=True)
    product_id: Optional[int] = Field(foreign_key="product.id", primary_key=True)
    user_id : Optional[int] = Field(foreign_key="user.id")

    user : Optional[User] = Relationship(back_populates="user")
    product: Optional[Product] = Relationship(back_populates="order_associations")
    order: Optional["OrderPurchase"] = Relationship(back_populates="product_associations")

class OrderPurchase(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id")
    total_amount: int

    user: Optional[User] = Relationship(back_populates="orders")
    product_associations: List[OrderProductLink] = Relationship(back_populates="order")
