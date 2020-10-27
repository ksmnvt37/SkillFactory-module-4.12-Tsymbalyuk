import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True )
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birth_date = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()
def request_data():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Введите пол: ")
    email = input("Введите адрес электронной почты: ")
    birth_date = input("Введите дату рождения: ")
    height = float(input("Введите рост: "))
    user_id = str(uuid.uuid4())
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birth_date=birth_date,
        height=height
    )
    return user

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()