import os
import glob
import pandas as pd


class Get_DataFrame():
    def __init__(self, path, title, column):
        self.path = path
        self.title = title
        self.column = column

    def get_df(self):

        dir_list = glob.glob(os.path.join(self.path,'*.xlsx'))

        dflist = []
        for i in dir_list:
            df = pd.read_excel(i)
            df = df[self.title ]
            dflist.append(df)

        df = pd.concat(dflist)
        df.columns = self.column
        return df

print("已生成DataFrame...")

# path_fyc = r"D:\work\基本法\人管系统基本法导出表\1_基础业绩查询"
# # dir_list = glob.glob(os.path.join(path_fyc,'*.xlsx'))

# column_name = ['month','dept','id','name','rank','fyc']
# fyc_title = ['结算月','部门名称','业务员代码','业务员姓名','职级','FYC']


# fyc = Fyc(path_fyc, fyc_title, column_name)
# fyc
