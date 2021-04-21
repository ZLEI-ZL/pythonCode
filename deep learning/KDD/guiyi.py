import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from pandas.core.frame import DataFrame
import numpy as np


x_train = pd.read_csv("x_train_1.csv", sep=',')
x_test = pd.read_csv('x_test_1.csv', sep=',')


print(x_train.shape)
print(x_test.shape)

def normalization(data):
    print('=' * 40)
    print('归一化数据')
    data['src_bytes'] = (data['src_bytes'] - data['src_bytes'].min()) / (data['src_bytes'].max() + 0.000001 - data['src_bytes'].min())
    data['dst_bytes'] = (data['dst_bytes'] - data['dst_bytes'].min()) / (data['dst_bytes'].max() + 0.000001 - data['dst_bytes'].min())
    data['count'] = (data['count'] - data['count'].min()) / (data['count'].max() + 0.000001 - data['count'].min())
    data['srv_count'] = (data['srv_count'] - data['srv_count'].min()) / (data['srv_count'].max() + 0.000001 - data['srv_count'].min())
    data['dst_host_count'] = (data['dst_host_count'] - data['dst_host_count'].min()) / (data['dst_host_count'].max() + 0.000001 - data['dst_host_count'].min())
    data['dst_host_srv_count'] = (data['dst_host_srv_count'] - data['dst_host_srv_count'].min()) / (data['dst_host_srv_count'].max() + 0.000001 - data['dst_host_srv_count'].min())
    #data['protocol_type'] = (data['protocol_type'] - data['protocol_type'].min()) / (data['protocol_type'].max() + 0.000001 - data['protocol_type'].min())
    # data['service'] = (data['service'] - data['service'].min()) / (data['service'].max() + 0.000001 - data['service'].min())
    # data['flag'] = (data['flag'] - data['flag'].min()) / (data['flag'].max() + 0.000001 - data['flag'].min())
    return data

x_train_1 = normalization(x_train)
x_test_1 = normalization(x_test)

x_train_1.to_csv('x_train_2.csv', index=False)
x_test_1.to_csv('x_test_2.csv', index=False)