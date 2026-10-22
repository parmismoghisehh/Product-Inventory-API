# Product Inventory Management API

A FastAPI application for managing a shop's product inventory.
Data is stored in memory and resets when the server restarts.

## Installation

Requires Python 3.10 or newer.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the API

```bash
python -m uvicorn main:app --reload
```

## Interactive documentation

Open http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint                  | Purpose                 |
| ------ | ------------------------- | ----------------------- |
| GET    | /products                 | List all products       |
| GET    | /products/search?name=lap | Search products by name |
| GET    | /products/{id}            | Retrieve one product    |
| POST   | /products                 | Create a product        |
| PUT    | /products/{id}            | Update a product        |
| DELETE | /products/{id}            | Delete a product        |

## Example product body

Use this JSON for POST and PUT:

```json
{
  "name": "Monitor",
  "category": "Electronics",
  "stock": 8,
  "price": 150,
  "description": "24-inch monitor"
}
```

The API generates product IDs automatically.
Description is optional.

## Expected responses

- 200: Successful retrieval, search, or update
- 201: Product created
- 204: Product deleted; no response body
- 404: Product not found
- 422: Invalid input
