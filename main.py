from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#Fields: id , name, price, stock, category, description
app=FastAPI()


class Products(BaseModel):
	name: str
	category: str
	stock: int
	price: float
	description: str
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
# to search products by name
@app.get("/products/search")
def Search(name:str):
	name=name.lower()
	result=[]
	for product in products:
		if name in product["name"].lower():
			result.append(product)
			raise HTTPException(status_code = 200 , details= "Successfully retreive all products")
			
	return {"query": name , "results": result}
#to return specific product
@app.get("/products/{id}") 
def GetProductID(id: str):
    for product in products:
        if str(product["id"]) == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# to create a new product
@app.post("/products")
def Create(category, description, name, id, stock, price):
	#users(admin) can add/create new product
    product = {
        "id": id,
        "name": name,
        "price": price,
        "stock": stock,
        "category": category,
        "description": description,
    }
    products.append(product)
    return product
#to update an existing product
@app.put("/products/{id}")
def Update(id: int, updated_product: Products):
    for index, product in enumerate(products):
        if str(product["id"]) == str(id):
            products[index] = {"id": product["id"], **updated_product.dict()}
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
	
	

    
