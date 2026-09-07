from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import create_engine,Column,Integer,String

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

# create table in database
Base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# create api

@app.post("/todos")
def create_todo(title:str,db: Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
    
# read data

@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todo = db.query(Todo).all()
    
    return {
        "Total":len(todo),
        "data": todo
    }
    
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first() 
    
    if not todo:
        raise HTTPException (
            status_code = 404 ,
            detail="Todo not Found"
        )
    return todo

#update data

@app.put("/todos/{todo_id}")
def update_data(todo_id:int,title:str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
            raise HTTPException (
                status_code = 404 ,
                detail="Todo not Found"
            )
    todo.title = title
    db.commit()
    db.refresh(todo)
    
    return {
        "message":"Todo updated",
        "data": todo
    }

# delete todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException (
            status_code = 404 ,
            detail="Todo not Found"
        )
    
    db.delete(todo)
    db.commit()
    
    return {
            "message":"Todo deleted",
            "data": todo
        }