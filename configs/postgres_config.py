from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

POSTGRES_SETTINGS = {
    "flask": {
        "HOST": "localhost",
        "PORT": 5432,
        "USERNAME": "postgres",
        "PASSWORD": "9d36SkmzYV3#dssblr34b",
        "DB": "db",
        "CONNECTOR": "psycopg2"
    }
}


def get_db_uri(CONNECTOR, USERNAME, PASSWORD, HOST, PORT, DB):
    return f'postgresql+{CONNECTOR}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'


def get_db_session(db) -> Session:
    return sessionmaker(ENGINES[db])()


DB_URI_UFA = get_db_uri(**POSTGRES_SETTINGS["flask"])

ENGINES = {
    "flask": create_engine(DB_URI_UFA, max_overflow=-1)
}

BASES = {
    "flask": declarative_base(ENGINES["flask"])
}
