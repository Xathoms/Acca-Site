from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,DATE

db = SQLAlchemy()
# def GeneratePasswordHash(pw,salt):
#     return sha256(pw.encode() + salt.encode()).hexdigest()
class PrenotationsDB(db.Model):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'Prenotations'.
    
    """

    __tablename__ = 'Prenotations'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    ChatID = Column(
        Integer,
        index=False,
        unique=False,
        nullable=False
    )
    Telefono = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    Nome = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    Cognome = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    Sesso = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    SessoPersonaggio = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    Gruppo = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    DataPrenotazione = Column(
        DATE,
        index=False,
        unique=False,
        nullable=False
    )


    def __repr__(self):
        return '<Prenotations {}>'.format(self.id)

class PrenotationsTables(db.Model):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'PrenotationsTables'.
    
    """

    __tablename__ = 'PrenotationsTables'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    Nome = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    MaxPeople = Column(
        Integer,
        index=False,
        unique=False,
        nullable=False,
        default=0
    )
    CurrentPeople = Column(
        Integer,
        index=False,
        unique=False,
        nullable=False,
        default=0
    )


    def __repr__(self):
        return '<EventsDates {}>'.format(self.id)

class EventsDates(db.Model):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'EventsDates'.
    
    """

    __tablename__ = 'EventsDates'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    Date = Column(
        DATE,
        index=False,
        unique=True,
        nullable=False
    )
    Name = Column(
        String(100),
        index=False,
        unique=False,
        nullable=False
    )
    TotPeople = Column(
        Integer,
        index=False,
        unique=False,
        nullable=False,
        default=0
    )


    def __repr__(self):
        return '<EventsDates {}>'.format(self.id)