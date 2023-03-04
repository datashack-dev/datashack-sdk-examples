from sqlalchemy import select
from my_app.models.users import Users

if __name__ == '__main__':
    # example how to query Users table with datashack + SQLAlchemy
    eng = Users.get_athena_engine()
    with eng.connect() as connection:
        table_obj = Users.get_table_obj(connection)
        result = connection.execute(select(table_obj).where(table_obj.c.age > 30).limit(10))
    print([r for r in result])
