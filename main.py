from typing import List
from db import SessionLocal
from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import crud
import schemas

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET
# @app.get("/items/{item_id}")
# def Get_Item(item_id: str):
#     _items = list(filter(lambda item: item['id'] == item_id, items)) # list that 'id' is item_i
#     if len(_items) == 0:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Item not found")
#     return _items[0]

@app.get("/items", response_model=List[schemas.Item])
def Get_Items(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)


@app.post("/items", response_model=schemas.Item)
def Create_Item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item=item)

# # PATCH

# @app.patch("/items") # 못찾으면 알아서 404 raise 시켜주네?
# def Update_Item(item: Item):
#     target = Get_Item(item.id)
#     target['name'] = item.name
#     return items

# # DELETE

# @app.delete("/items") # 못찾으면 알아서 404 raise 시켜주네?
# def Delete_Item(item: Item):
#     target = Get_Item(item.id)
#     items.pop(items.index(target))
#     return items
