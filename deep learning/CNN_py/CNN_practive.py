import tensorflow as tf
import os
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.layers import Conv1D, BatchNormalization, Activation, MaxPool1D, Dropout, Flatten, Dense
import pandas as pd
from sklearn.preprocessing import Normalizer

batch_size = 128  #一批训练样本128张图片
num_classes = 40  #有40个类别
epochs = 20   #迭代轮数
init_lr = 0.0001  #学习率
input_shape = (118,1) # 输入shape
validation_split = 0.2


x_train = pd.read_csv('D:\pythonCode\deep learning\KDD\\x_train_2.csv').values
y_train = pd.read_csv('D:\pythonCode\deep learning\KDD\\y_train_2.csv').values
x_test = pd.read_csv('D:\pythonCode\deep learning\KDD\\x_test_2.csv').values
y_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_test.csv').values

# x_test = np.delete(x_test, 0, axis=1)
# y_test = np.delete(y_test, 0, axis=1)
# x_train = np.delete(x_train, 0, axis=1)
# y_train = np.delete(y_train, 0, axis=1)

x_train = np.expand_dims(x_train, axis=2)
x_test = np.expand_dims(x_test, axis=2)


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


##print(x_train[0])
print('x_train.shape:', x_train.shape)
print('y_train.shape:', y_train.shape)

model = tf.keras.models.Sequential()
model.add(Conv1D(filters=30, kernel_size=3, strides=1, kernel_regularizer=tf.keras.regularizers.L1(), input_shape=input_shape, activation='relu'))
model.add(Conv1D(filters=64, kernel_size=3, strides=1, kernel_regularizer=tf.keras.regularizers.L1(), activation='relu'))
#model.add(Activation('relu'))
model.add(MaxPool1D(pool_size= 3, strides=1))
#model.add(Conv1D(filters=128, kernel_size=3, strides=1, activation='relu'))
#model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=init_lr),
               loss='categorical_crossentropy', metrics=['accuracy'])


#加入checkpoint
# checkpoint_save_path = "./checkpoint/CNN_practive.ckpt"  # checkpoint保存位置
# if os.path.exists(checkpoint_save_path + '.index'):
#     print('-------------load the model-----------------')
#     model.load_weights(checkpoint_save_path)

# cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
#                                                  save_weights_only=True,
#                                                  save_best_only=True)

history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
                    validation_split=validation_split,
                    validation_freq=1,
                    #callbacks=checkpoint_save_path
                    )

model.summary()

#print(model.trainable_variables)  #打印权重
#权重存取.txt
file = open('./CnnWeights.txt', 'w')
for v in model.trainable_variables:
    file.write(str(v.name) + '\n')
    file.write(str(v.shape) + '\n')
    file.write(str(v.numpy()) + '\n')
file.close()

print('------------------ Save Model ------------------')
model.save('./model_CNN_KddCup99.h5')


print('------------------ Load Model ------------------')
newModel = tf.keras.models.load_model('model_CNN_KddCup99.h5')  #载入模型

score = newModel.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# predict_test = newModel.predict(x_test)  #预测X获得Y
# #print(predict_test)
# y_test_pred = np.argmax(predict_test, axis=1)  #输出最大可能性的
# #print(y_test_pred)
# y_test = y_test.reshape(y_test.shape[0] * y_test.shape[1])  #将y_test变成一维，与y_test_pred同维
# #print(y_test)
# print('True number: ', (sum(y_test_pred == y_test)))
# print('Test accuracy: %f' % (float((sum(y_test_pred == y_test))) / float(y_test.shape[0])))


# 显示训练集和验证集的acc和loss曲线
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.subplot(1,2,1)
plt.plot(acc, label='Train Accuracy')
plt.plot(val_acc, label='Val Accuracy')
#plt.plot(score[1], label='Test Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(loss, label='Train Loss')
plt.plot(val_loss, label='Val Loss')
#plt.plot(score[0], label='Test Loss')
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
