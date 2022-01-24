from calendar import month
import os
import glob
import pandas as pd

import sys
sys.path.append(r'..')
from get_df.get_df import Get_DataFrame

from sqlalchemy import create_engine #create_engine
from sqlalchemy.ext.declarative import declarative_base #declarative_base
from sqlalchemy import Column, Integer, String, Float, DECIMAL, Boolean, Enum, Date, DateTime, Time #要导入用到的数据类型
from sqlalchemy import Index, UniqueConstraint #唯一约束、多列约束
import datetime

path_fyc = r"D:\work\project\data\基本法\1_基础业绩查询"
column_name = ['month','dept','id','name','rank','fyc']
fyc_title = ['结算月','部门名称','业务员代码','业务员姓名','职级','FYC']

f = Get_DataFrame(path_fyc, fyc_title, column_name)
fyc = f.get_df()

#建立SQLAlchemy连接
engine = create_engine("mysql+pymysql://admin_001:Mlc870621@@rm-uf6slgt4e14ql190elo.mysql.rds.aliyuncs.com:3306/cpic")
Base = declarative_base()

class DealRecord(Base):
    
    __tablename__ = "kpi_基础业绩查询_sys"

    Index = Column(Integer)
    month = Column(Date)
    dept = Column(String(32))
    id = Column(String(32),primary_key=True)
    name = Column(String(32))
    rank = Column(String(32))
    fyc = Column(Float)   

    # 元信息，相当于Django的ORM的class Meta
    __table_args__ = (
        UniqueConstraint("Index","id", "name", name="uni_id_name"),
#         Index("name", "email")
    )
def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(engine)


def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_db()

try:
    fyc.to_sql('kpi_基础业绩查询_sys',engine,if_exists='replace')
    print("成功导入")
except IOError:
    print("未能成功导入")