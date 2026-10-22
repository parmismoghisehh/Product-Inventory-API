from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#Fields: id , name, price, stock, category, description
app=FastAPI()


class Products(BaseModel):
	name: str
	category: str
	stock: int
	price: float
	description: Optional[str] = None
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 750,
        "stock": 5,
        "category": "Electronics",
        "description": "15-inch laptop"
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 25,
        "stock": 20,
        "category": "Accessories",
        "description": "Wireless mouse"
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 45,
        "stock": 10,
        "category": "Accessories",
        "description": "Mechanical keyboard"
    }
]
#to return all products

@app.get("/products")#passed
def GetProducts():
	return products



# to create a new product
@app.post("/products")
def Create(new_product: Products):
    product = {
        "id": max((int(existing["id"]) for existing in products), default=0) + 1,
        **new_product.dict(),
    }
    products.append(product)
    raise HTTPException(status_code=201 , detail="New product created successfully")
    return product
#to update an existing product
@app.put("/products/{id}")
def Update(id: int, updated_product: Products):
    for index, product in enumerate(products):
        if str(product["id"]) == str(id):
            products[index] = {
                **product,
                **updated_product.dict(exclude_unset=True),
                "id": product["id"],
            }
            return products[index]
    raise HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
# to delete an existing product
@app.delete("/products")
def Delete(id: int):
    for index, product in enumerate(products):
        if str(product["id"]) == str(id):
            products.pop(index)
            return {"detail": "Product has been deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
# to search products by name
@app.get("/products/search")
def Search(name: str):
    result = []
    for product in products:
        if name.lower() in product["name"].lower():
            result.append(product)
    return result

#to return specific product
@app.get("/products/{id}")
def GetProductID(id: str):
    for product in products:
        if str(product["id"]) == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")