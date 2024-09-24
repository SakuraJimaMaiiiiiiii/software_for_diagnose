#用于接口调用诊断
import joblib
import pandas as pd
import numpy as np
import math

def get_excel_feature(column,data):
    '''
    :param column: 需要读取的excel列
    :param data: excel表格数据
    :return:
    '''
    feature=[]
    #定义获取某一列的时域特征的函数，输入为一维的Dataframe格式的数据
    def get_time_domain_features(data):
        '''data为一维振动信号'''
        fea = []
        len_ = len(data)
        mean_ = data.mean()  # 1.均值
        var_ = data.var()  # 2.方差
        std_ = data.std()  # 3.标准差
        max_ = data.max()  # 4.最大值
        min_ = data.min()  # 5.最小值
        x_p = max(abs(max_), abs(min_))  # 峰值
        x_rms = math.sqrt((data ** 2).sum() / len_)  # 均方根值
        x_r = ((abs(data) ** 0.5).sum() / len_) ** 2  # 方根幅值
        W = x_rms / mean_  # 波形指标
        C = x_p / x_rms  # 峰值指标
        I = x_p / mean_  # 脉冲指标
        L = x_p / x_r  # 裕度指标
        S = ((data - mean_) ** 3).sum() / ((len_ - 1) * std_ ** 3)  # 偏斜度
        K = ((data - mean_) ** 4).sum() / ((len_ - 1) * std_ ** 4)  # 峭度
        fea = [mean_,var_,std_,max_,min_,x_p, x_rms, x_r, W, C, I, L, S, K]
        return fea
    for i in column:
        feature.append(get_time_domain_features(data[i]))
    feature = np.concatenate(feature, axis=0)
    return feature.reshape(1,-1)

class RFzhenduan():
    def __init__(self):
        self.columns = ['大气舱绝压(kPaA)', '高度(m)', '座舱绝压(kPaA)', '座舱余压(kPaA)', '总流量(kg/h)',
                   '控制腔压力(kPaA)']
        self.dir = {0: '进气量不足', 1: '进气量过多', 2: '进气量波动', 3: '高度保护堵塞', 4: '减震器漏气', 5: '绝压堵塞',
               6: '定径孔堵塞', 7: '控制腔泄露到大气', 8: '控制腔泄露到高保', 9: '排气活门堵塞', 10: '余压堵塞',
               11: '座舱泄露', 12: '正常'}
    def zhenduan(self,filename,modelname):
        RFclf = joblib.load(modelname)
        exceldata = pd.read_excel(filename)
        excelfeature = get_excel_feature(self.columns, exceldata)  # 特征提取
        a = RFclf.predict(excelfeature)
        return self.dir[a[0]]




if __name__ == "__main__":
    k = RFzhenduan()
    k.zhenduan(filename=r'E:\files\项目\新乡\lpy_guzhangdata_excel\kongzhiqiang_dingjingkong_duse\newdata1_0.02mm\30.xlsx', modelname='rf.model')