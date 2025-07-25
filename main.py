from database import SessionLocal, engine, Base
import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
print("Table is created")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating Routes
app = FastAPI()

@app.post("/items/", response_model= schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item= crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item NOT FOUND")
    return item

@app.put("/items/{item_id}", response_model= schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session= Depends(get_db)):
    updated_item = crud.update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item NOT FOUND")
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session= Depends(get_db)):
    deleted_item = crud.delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item NOT FOUND")
    return {"details": "Deleted"}
    