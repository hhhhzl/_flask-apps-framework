from email.policy import default
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Numeric
from sqlalchemy import inspect, UniqueConstraint
from configs.postgres_config import ENGINES, BASES, get_db_session

# add model
class App1_model1(BASES['flask']):
    pass


class App1_model2(BASES['flask']):
    pass


class App1_model3(BASES['flask']):
    pass


if __name__ == "__main__":
    pass
