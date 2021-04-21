import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from pandas.core.frame import DataFrame
import numpy as np

# 读入
def readData():
    col_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment",
                 "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted",
                 "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
                 "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
                 "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
                 "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
                 "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
                 "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]  # 42个标识

    data_percent_10 = pd.read_csv("D:\pythonCode\deep learning\CNN_py\kddcup\kddcup.data_10_percent.txt", sep=',', header=None, names=col_names)
    #print(data_percent_10.head(10))
    #data_percent_10.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\data_percent_10.csv')

    data_corrected = pd.read_csv("D:\pythonCode\deep learning\CNN_py\kddcup\corrected.txt", sep=',', header=None, names=col_names)
    #print(data_corrected.head(10))
    #data_corrected.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\data_corrected.csv')
    return data_percent_10, data_corrected

# 将字符型数据数值化
def transStrToNum(data):
    print('='*40)
    print('数值化数据')
    # print(data_p)
    # print(data_c)
    data['protocol_type'] = data['protocol_type'].map({'tcp': 0, 'udp': 1, 'icmp': 2})

    # 将源文件中70种网络服务类型转换成数字标识
    data['service'] = data['service'].map(
        {'aol': 0, 'auth': 1, 'bgp': 2, 'courier': 3, 'csnet_ns': 4, 'ctf': 5, 'daytime': 6, 'discard': 7, 'domain': 8,
         'domain_u': 9, 'echo': 10, 'eco_i': 11, 'ecr_i': 12, 'efs': 13, 'exec': 14, 'finger': 15, 'ftp': 16,
         'ftp_data': 17, 'gopher': 18, 'harvest': 19, 'hostnames': 20, 'http': 21, 'http_2784': 22, 'http_443': 23,
         'http_8001': 24, 'imap4': 25, 'IRC': 26, 'iso_tsap': 27, 'klogin': 28, 'kshell': 29, 'ldap': 30, 'link': 31,
         'login': 32, 'mtp': 33, 'name': 34, 'netbios_dgm': 35, 'netbios_ns': 36, 'netbios_ssn': 37, 'netstat': 38,
         'nnsp': 39, 'nntp': 40, 'ntp_u': 41, 'other': 42, 'pm_dump': 43, 'pop_2': 44, 'pop_3': 45, 'printer': 46,
         'private': 47, 'red_i': 48, 'remote_job': 49, 'rje': 50, 'shell': 51, 'smtp': 52, 'sql_net': 53, 'ssh': 54,
         'sunrpc': 55, 'supdup': 56, 'systat': 57, 'telnet': 58, 'tftp_u': 59, 'tim_i': 60, 'time': 61, 'urh_i': 62,
         'urp_i': 63, 'uucp': 64, 'uucp_path': 65, 'vmnet': 66, 'whois': 67, 'X11': 68, 'Z39_50': 69})

    # 将源文件中11种网络连接状态转换成数字标识
    data['flag'] = data['flag'].map(
        {'OTH': 0, 'REJ': 1, 'RSTO': 2, 'RSTOS0': 3, 'RSTR': 4, 'S0': 5, 'S1': 6, 'S2': 7, 'S3': 8, 'SF': 9, 'SH': 10})

    # 将源文件中攻击类型转换成数字标识(训练集中共出现了22个攻击类型，而剩下的17种只在测试集中出现)
    data['label'] = data['label'].map(
        {'normal.': 0, 'ipsweep.': 1, 'mscan.': 2, 'nmap.': 3, 'portsweep.': 4, 'saint.': 5, 'satan.': 6, 'apache2.': 7,
         'back.': 8, 'land.': 9, 'mailbomb.': 10, 'neptune.': 11, 'pod.': 12, 'processtable.': 13, 'smurf.': 14,
         'teardrop.': 15, 'udpstorm.': 16, 'buffer_overflow.': 17, 'httptunnel.': 18, 'loadmodule.': 19, 'perl.': 20,
         'ps.': 21, 'rootkit.': 22, 'sqlattack.': 23, 'xterm.': 24, 'ftp_write.': 25, 'guess_passwd.': 26, 'imap.': 27,
         'multihop.': 28, 'named.': 29, 'phf.': 30, 'sendmail.': 31, 'snmpgetattack.': 32, 'snmpguess.': 33, 'spy.': 34,
         'warezclient.': 35, 'warezmaster.': 36, 'worm.': 37, 'xlock.': 38, 'xsnoop.': 39})

    return data

def one_hot_Data(data):
    enc = OneHotEncoder(sparse = False)  #独热编码
    enc.fit([[0], [1], [2]]) # 三种协议类型
    data['protocol_type'] = DataFrame(enc.transform(data[['protocol_type']]))

    enc.fit([[0],[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19],
         [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37],
         [38], [39],[40],[41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59],
         [60], [61], [62], [63], [64], [65], [66], [67], [68], [69]])  # 70种网络服务类型
    data['service'] = DataFrame(enc.transform(data[['service']]))

    enc.fit([[0],[1], [2], [3], [4], [5], [6], [7], [8], [9],[10]])  #11种网络连接状态
    data['flag'] = DataFrame(enc.transform(data[['flag']]))

    enc.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19],
         [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37],
         [38], [39]])  #有40种元素
    data['label'] = DataFrame(enc.transform(data[['label']]))
    return DataFrame(data)

def one_hot_label(data):
    enc = OneHotEncoder(sparse=False)
    enc.fit([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19],
         [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37],
         [38], [39]])
    #print(data.shape)

    data = enc.transform(data.values.reshape(-1, 1))
    return DataFrame(data)

# 归一化数据
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
    data['service'] = (data['service'] - data['service'].min()) / (data['service'].max() + 0.000001 - data['service'].min())
    data['flag'] = (data['flag'] - data['flag'].min()) / (data['flag'].max() + 0.000001 - data['flag'].min())
    return data

def get_train(data):
    print('=' * 40)
    print('获得训练集')
    data = transStrToNum(data)  #测试集数值化
    #data = one_hot_Data(data)  #独热编码
    data = normalization(data)  #归一化
    #print(type(data))

    data_x = data.iloc[:, 0:40]  # 取前40列
    #print(data_x.shape)
    data_y = data.iloc[:, 41]  # 取41列
    #print(data_y.shape)
    data_y = one_hot_label(data_y)
    return data_x, data_y

def get_corrected(data):
    print('=' * 40)
    print('获得测试集')
    data = transStrToNum(data)  # 测试集数值化
    #data = one_hot_Data(data)  # 独热编码
    data = normalization(data)  # 归一化

    data_x = data.iloc[:, 0:40]
    data_y = data.iloc[:, 41]
    data_y = one_hot_label(data_y)
    #data_y = one_hot_label(data_y)
    return data_x, data_y

def dataToCsv(x_train, y_train, x_test, y_test):
    print(type(x_train))
    x_train.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\x_train.csv', index=False)
    y_train.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_train.csv', index=False)
    x_test.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\x_test.csv', index=False)
    y_test.to_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_test.csv', index=False)

if __name__ == '__main__':
    data_percent_10, data_corrected = readData()  # 获取数据集和测试集

    x_train, y_train = get_train(data_percent_10)

    x_test, y_test = get_corrected(data_corrected)
    print('='*40)
    print('x_train.shape:', x_train.shape)
    print('y_train.shape:', y_train.shape)
    print(type(x_train))

    dataToCsv(x_train, y_train, x_test, y_test)
    print('=' * 40)
    print('datasets ok')

