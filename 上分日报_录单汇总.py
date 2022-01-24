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

path_daily = r"D:\work\project_data\上分日报"
column_name = ['id','name','claim_name','pay_period','prem','claim_date','excu_date']
deal_rec_title = ['业务员代码','姓名','险种名称','保费','投保日期','生效日期']

df = Get_DataFrame(path_daily, deal_rec_title, column_name)
deal_rec = df.get_df()


#建立SQLAlchemy连接
engine = create_engine("mysql+pymysql://admin_001:Mlc870621@@rm-uf6slgt4e14ql190elo.mysql.rds.aliyuncs.com:3306/cpic",)
Base = declarative_base()

class DealRecord(Base):
    
    __tablename__ = "kpi_deal_record"

    # primary_key主键、index索引、nullable是否可以为空
    Index = Column(Integer,primary_key=True)
    id = Column(String(32))
    name = Column(String(32))
#     bd_num = Column(String(32))
    pay_period = Column(DateTime, default=datetime.datetime.now)
    prem = Column(Float)
    claim_date = Column(Date)
    excu_date = Column(Date)
    

#     # 元信息，相当于Django的ORM的class Meta
#     __table_args__ = (
#         UniqueConstraint("Index","id", "name", name="uni_id_name"),
# #         Index("name", "email")
#     )
def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(engine)


def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(engine)



if __name__ == '__main__':
    create_db()
    

try:
    deal_rec.to_sql('kpi_deal_record',engine,if_exists='replace')
    print("成功导入")
except IOError:
    print("未能成功导入")