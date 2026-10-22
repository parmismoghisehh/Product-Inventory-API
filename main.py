from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#Fields: id , name, price, stock, category, description
app=FastAPI()

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
class Products(BaseModel):
	id: str
	name: str
	category: str
	stock: int
	price: float
	description: str
#to return all products
data={}
@app.get("/products")
def GetProducts(category: str, description: str, name: str, id: int, stock: int, price: float):
	return {
		"id": id,
		"name": name,
		"price": price,
		"stock": stock,
		"category": category,
		"description": description,
	}
#to return specific product
@app.get("/products/{id}") 
def GetProductID(
	id: str,
	name: str,
	price: float,
	stock: int,
	category: str,
	description: str,
):
	if id in products:
		return{
			"id": id,
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "category": category,
                    "description": description,
        }
	else:
		raise HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
# to search products by name
@app.get("/products/search")
def Search(name:str):
	name=name.lower()
	result=[]
	for product in products:
		if name in product["name"].lower():
			result.append(product)
			raise HTTPException(code_status = 200 , details= "Successfully retreive all products")
			
	return {"query": name , "results": result}
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
        if product["id"] == id:
            products[index] = updated_product.dict()
            return products[index]
    raise HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
# to delete an existing product
@app.delete("/products")
def Delete(id: int):
    for index, product in enumerate(products):
        if product["id"] == id:
            products.pop(index)
            return {"detail": "Product has been deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
	
	

    

