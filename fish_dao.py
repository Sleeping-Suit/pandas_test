import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data.fish_api import getTrains, getTests

engine = db.create_engine("mariadb+mariadbconnector://fish:fish1234@127.0.0.1:3306/fishdb")

# train insert/select
def train_Insert():
    trains = getTrains()
    trains.to_sql("train", engine, index=False, if_exists="replace")

def train_Select():
    df = pd.read_sql(sql="select * from train", con=engine)
    print(df)

# test insert/select
def test_Insert():
    tests = getTests()
    tests.to_sql("test", engine, index=False, if_exists="replace")

def test_Select():
    df = pd.read_sql(sql="select * from test", con=engine)
    print(df)


train_Insert()
test_Insert()