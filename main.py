from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import crud, schemas
from DBConfig import SessionLocal
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=schemas.User)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{chat_id}", response_model=schemas.User)
def read_user(chat_id: int, db: Session = Depends(get_db)):
    this_date = crud.get_this_date(db)
    last_date = crud.get_last_date(db)
    db_user = crud.get_user(
        db, chat_id=chat_id, this_date=this_date.Date, last_date=last_date.Date
    )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        # host=settings.HOST,
        reload=True,
        # port=settings.PORT,
    )
