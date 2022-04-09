from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4'.format('xathoms', 'Xath3488', '195.231.19.190', '3306','ACCA'),pool_pre_ping=True,pool_recycle=3600,echo_pool=True,pool_size=10, max_overflow=20)

session = Session(engine)