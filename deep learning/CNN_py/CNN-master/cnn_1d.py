from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.layers import Conv1D,GlobalAveragePooling1D,MaxPooling1D
import matplotlib.pyplot as plt
# 以下为数据加载部分
import numpy as np
import pandas as pd
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from sklearn.preprocessing import Normalizer


# #训练集
# train_data=pd.read_csv('data/ga_kdd99/train_10percent.csv',header=None)
# #测试集
# test_data=pd.read_csv('data/ga_kdd99/test20000.csv',header=None)
# #训练集训练部分
# train=train_data.iloc[:,0:8]
# #训练集标签
# train_lb=train_data.iloc[:,9]
# #测试集测试部分
# test=test_data.iloc[:,0:8]
# #测试集标签
# test_lb=test_data.iloc[:,9]
# #归一化训练集和测试集
# scaler=Normalizer().fit(train)
# x_train=scaler.transform(train)
# scaler=Normalizer().fit(test)
# x_test=scaler.transform(test)
# x=np.expand_dims(x_train,axis=2)
# y=np.expand_dims(x_test,axis=2)
# #标签数组化
# tr_lb=np.reshape(train_lb,494021)
# te_lb=np.reshape(test_lb,20000)

x_train = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\x_train.csv').values
y_train = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_train.csv').values
x_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\x_test.csv').values
y_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_test.csv').values

x_test = np.delete(x_test, 0, axis=1)
y_test = np.delete(y_test, 0, axis=1)
x_train = np.delete(x_train, 0, axis=1)
y_train = np.delete(y_train, 0, axis=1)

x = np.expand_dims(x_train, axis=2)
y = np.expand_dims(x_test, axis=2)

#构建模型
cnn_1D=Sequential()
cnn_1D.add(Conv1D(64,1,activation='relu',input_shape=(40,1)))
cnn_1D.add(Conv1D(64,1,activation='relu'))
cnn_1D.add(MaxPooling1D(3))
cnn_1D.add(Conv1D(64,1,activation='relu'))
cnn_1D.add(Conv1D(64,1,activation='relu'))
cnn_1D.add(GlobalAveragePooling1D())
cnn_1D.add(Dropout(0.5))
cnn_1D.add(Dense(40,activation='softmax'))
cnn_1D.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=(['accuracy'])
)
history = cnn_1D.fit(x,y_train,batch_size=80, epochs=15, validation_split=(0.2), validation_freq=1)
score=cnn_1D.predict(y)
score = np.argmax(score, axis=1)
y_test = y_test.reshape(y_test.shape[0] * y_test.shape[1])  #将y_test变成一维，与y_test_pred同维
#print(y_test)
print('True number: ', (sum(score == y_test)))
print('Test accuracy: %f' % (float((sum(score == y_test))) / float(y_test.shape[0])))
print(score)
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.subplot(1,2,1)
plt.plot(acc, label='Train Accuracy')
plt.plot(val_acc, label='Val Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(loss, label='Train Loss')
plt.plot(val_loss, label='Val Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()
