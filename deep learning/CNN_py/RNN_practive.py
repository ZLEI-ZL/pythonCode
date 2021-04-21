import tensorflow as tf
import os
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding, Dropout
import pandas as pd


batch_size = 128  #一批训练样本128张图片
num_classes = 40  #有40个类别
epochs = 10   #迭代轮数
init_lr = 0.001  #学习率
input_shape = (118,1) # 输入shape
validation_split = 0.2


x_train = pd.read_csv('D:\pythonCode\deep learning\KDD\\x_train_2.csv').values
y_train = pd.read_csv('D:\pythonCode\deep learning\KDD\\y_train_2.csv').values
x_test = pd.read_csv('D:\pythonCode\deep learning\KDD\\x_test_2.csv').values
y_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_test.csv').values



#随机数种子，保证数据和标签打乱顺序一致
seed_1=77
np.random.seed(seed_1)
np.random.shuffle(x_train)
np.random.seed(seed_1)
np.random.shuffle(y_train)

seed_2=78
np.random.seed(seed_2)
np.random.shuffle(x_test)
np.random.seed(seed_2)
np.random.shuffle((y_test))

x_train = np.expand_dims(x_train, axis=2)
x_test = np.expand_dims(x_test, axis=2)

# # print(x_train[0])
# print('x_train.shape:', x_train.shape)
# print('y_train.shape:', y_train.shape)

#创建模型
model = tf.keras.models.Sequential()
#model.add(Embedding(len(x_train)*40, 32))  #Embedding编码，32维表示数据
model.add(SimpleRNN(32, activation='relu', return_sequences=True))  # 添加RNN层
model.add(SimpleRNN(64, activation='relu', return_sequences=True))
model.add(SimpleRNN(32, activation='relu', return_sequences=False))
Dropout(0.2)  # 随机丢弃0.2神经元
model.add(Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.L1()))  # 全连接层
model.add(Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.L1()))
model.add(Dense(num_classes, activation='softmax', kernel_regularizer=tf.keras.regularizers.L1()))  # 输出层


model.compile(optimizer=tf.keras.optimizers.Adam(lr=init_lr),
              loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
                    validation_split=validation_split, validation_freq=1)

model.summary()  #打印网络summary


# 保存权重
file = open('./RnnWeights.txt', 'w')
for v in model.trainable_variables:
    file.write(str(v.name) + '\n')
    file.write(str(v.shape) + '\n')
    file.write(str(v.numpy()) + '\n')
file.close()

print('------------------ Save Model ------------------')
model.save('./model_RNN_KddCup99.h5')


print('------------------ Load Model ------------------')
newModel = tf.keras.models.load_model('model_RNN_KddCup99.h5')

score = newModel.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# predict_test = newModel.predict(x_test)  #预测测试集
# y_test_pred = np.argmax(predict_test, axis=1)
# y_test = y_test.reshape(y_test.shape[0] * y_test.shape[1])  #将y_test变成一维，与y_test_pred同维
# #print(y_test)
# print('True number: ', (sum(y_test_pred == y_test)))
# print('test accuracy: %f' % (float((sum(y_test_pred == y_test))) / float(y_test.shape[0])))



# 显示训练集和验证集的acc和loss曲线
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

# x = []
# for i in range(len(x_test)):
#     x.append(i)
# plt.subplot(1,3,3)
# plt.scatter(x, y_test, label='Y_test', color='blue')
# plt.plot(y_test_pred, label='predict y_test', color='red')
# plt.xlabel('the number of data')
# plt.ylabel('differency of y_test and y_test_pred')
# plt.legend()
# plt.show()