from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    ChatID: int
    Telefono: str
    Nome: str
    Cognome: str
    Sesso: str
    SessoPersonaggio: str
    Gruppo: str
    DataPrenotazione: date


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TableBase(BaseModel):
    Nome: str
    MaxPeople: int
    CurrentPeople: int


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int

    class Config:
        orm_mode = True
        
class EventBase(BaseModel):
    Date: date
    Name: str
    TotPeople: int


class EventeCreate(EventBase):
    pass


class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
