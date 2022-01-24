import os
import glob
import pandas as pd
import pymysql

import sys
sys.path.append(r'..')
from get_df.get_df import Get_DataFrame

from sqlalchemy import create_engine #create_engine
from sqlalchemy.ext.declarative import declarative_base #declarative_base
from sqlalchemy import Column, Integer, String, Float, DECIMAL, Boolean, Enum, Date, DateTime, Time #要导入用到的数据类型
from sqlalchemy import Index, UniqueConstraint #唯一约束、多列约束
import datetime

path_daily = r"D:\work\project\data\基本法\1_缴费记录查询_多"
deal_rect_title = ['业务员代码','姓名','职级','渠道','业务员状态','签约日期','保单号','险种代码','险种名称','险种类别名称','投保日期','生效日期','缴费年限','FYC','保费','佣金率','标准保费','折标系数']
column_name = ['id','name','rank','channel','status','enroll_date','claim_num','ins_code','ins_name','ins_cat','selling_date','excu_date','pay_period','fyc','premium','comm_rate','standard_premium','ps_coeff']

"""实例化"""
df = Get_DataFrame(path_daily, deal_rect_title, column_name)
deal_rec_sys = df.get_df()

#建立SQLAlchemy连接
engine = create_engine("mysql+pymysql://admin_001:Mlc870621@@rm-uf6slgt4e14ql190elo.mysql.rds.aliyuncs.com:3306/cpic")
Base = declarative_base()

class DealRecord(Base):
    
    __tablename__ = "kpi_缴费记录查询_sys"

    Index = Column(Integer,primary_key=True)
    id = Column(String(32))
    name = Column(String(32))
    rank = Column(String(32))
    channel = Column(String(32))
    status = Column(String(32))
    enrolling_date = Column(String(32))
    claim_num = Column(String(32))
    ins_code = Column(String(32))
    ins_name = Column(String(32))
    ins_cat = Column(String(32))
    selling_date = Column(Date)
    excu_date = Column(Date)
    pay_period = Column(DateTime, default=datetime.datetime.now)
    fyc = Column(Float)
    premimum = Column(Float)
    comm_rate = Column(Float)
    standard_premium = Column(Float)
    ps_coeff = Column(Float)
    

    # 元信息，相当于Django的ORM的class Meta
    __table_args__ = (
        UniqueConstraint("Index","id", "name",'claim_num','ins_name', name="uni_id_name"),
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
    deal_rec_sys.to_sql('kpi_缴费记录查询_sys',engine,if_exists='replace')
    print("成功导入")
except IOError:
    print("未能成功导入")