from DBConfig import Base
from sqlalchemy import Column, Integer, String, DATE


class PrenotationsDB(Base):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'Prenotations'.

    """

    __tablename__ = "Prenotations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ChatID = Column(Integer, index=False, unique=False, nullable=False)
    Telefono = Column(String(100), index=False, unique=False, nullable=False)
    Nome = Column(String(100), index=False, unique=False, nullable=False)
    Cognome = Column(String(100), index=False, unique=False, nullable=False)
    Sesso = Column(String(100), index=False, unique=False, nullable=False)
    SessoPersonaggio = Column(String(100), index=False, unique=False, nullable=False)
    Gruppo = Column(String(100), index=False, unique=False, nullable=False)
    DataPrenotazione = Column(DATE, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<Prenotations {}>".format(self.Nome)


class PrenotationsTables(Base):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'PrenotationsTables'.

    """

    __tablename__ = "PrenotationsTables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String(100), index=False, unique=False, nullable=False)
    MaxPeople = Column(Integer, index=False, unique=False, nullable=False, default=0)
    CurrentPeople = Column(
        Integer, index=False, unique=False, nullable=False, default=0
    )

    def __repr__(self):
        return "<EventsDates {}>".format(self.Nome)


class EventsDates(Base):
    """
    Data model for ACCA entity.
    This class, handle the creation,insert,delete or update of the database table 'EventsDates'.

    """

    __tablename__ = "EventsDates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(DATE, index=False, unique=True, nullable=False)
    Name = Column(String(100), index=False, unique=False, nullable=False)
    TotPeople = Column(Integer, index=False, unique=False, nullable=False, default=0)

    def __repr__(self):
        return "<EventsDates {}>".format(self.Name)
