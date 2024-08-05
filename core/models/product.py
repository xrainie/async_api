from .base import BaseModel
from sqlalchemy.orm import Mapped


class ProductModel(BaseModel):
    id: Mapped[int]
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
