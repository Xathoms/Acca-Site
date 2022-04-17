from datetime import date
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, chat_id: int, this_date: date, last_date: date):
    return (
        db.query(models.PrenotationsDB)
        .filter(
            models.PrenotationsDB.ChatID == chat_id,
            models.PrenotationsDB.DataPrenotazione <= this_date,
            models.PrenotationsDB.DataPrenotazione >= last_date,
        )
        .first()
    )


def get_this_date(db: Session):
    return db.query(models.EventsDates).order_by(models.EventsDates.Date.desc()).first()


def get_last_date(db: Session):
    return (
        db.query(models.EventsDates)
        .filter(
            models.EventsDates.Date
            < db.query(models.EventsDates)
            .order_by(models.EventsDates.Date.desc())
            .first().Date
        )
        .order_by(models.EventsDates.Date.desc())
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PrenotationsDB).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.PrenotationsDB(
        ChatID=user.ChatID,
        Telefono=user.Telefono,
        Nome=user.Nome,
        Cognome=user.Cognome,
        Sesso=user.Sesso,
        SessoPersonaggio=user.SessoPersonaggio,
        Gruppo=user.Gruppo,
        DataPrenotazione=user.date,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
