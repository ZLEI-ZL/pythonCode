import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\x_test.csv').values
y_test = pd.read_csv('D:\pythonCode\deep learning\CNN_py\kddcup\\y_test.csv').values
x_test = np.delete(x_test, 0, axis=1)
y_test = np.delete(y_test, 0, axis=1)
x_test = np.expand_dims(x_test, axis=2)

print(x_test.shape)
#print(x_test[0:3])
# print(x_test[0].shape)
# x = np.expand_dims(x_test[0], axis=0)
# print(x.shape)
newModel = tf.keras.models.load_model('model_CNN_KddCup99.h5')  #载入模型

predict_test = newModel.predict(x_test)  #预测X获得Y
#print(predict_test)
y_test_pred = np.argmax(predict_test, axis=1)  #输出最大可能性的
#print(y_test_pred)
y_test = y_test.reshape(y_test.shape[0] * y_test.shape[1])  #将y_test变成一维，与y_test_pred同维
#print(y_test)
#print((sum(y_test_pred == y_test)), type((sum(y_test_pred == y_test))))
print('test accuracy: %f' % (float((sum(y_test_pred == y_test))) / float(y_test.shape[0])))

# # plt.subplot(1,3,3)
# print(len(x_test))
x = []
for i in range(len(x_test)):
    x.append(i)
# print(x)
# y_test_pred_a = y_test_pred.reshape(-1, 1)
# y_test_a = y_test.reshape(-1, 1)
# print(y_test_a)

plt.scatter(x[0:200], y_test[0:200], label='Y_test', color='blue')
plt.plot(y_test_pred[0:200], label='predict y_test', color='red')
plt.xlabel('the number of data')
plt.ylabel('differency of y_test and y_test_pred')
plt.legend()
plt.show()