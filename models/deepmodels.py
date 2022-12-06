'''
这里搞点deep模型
用tensorflow吧
'''
import tensorflow as tf
import matplotlib.pyplot as plt
X = tf.random.normal([100, 1]).numpy()
noise = tf.random.normal([100, 1]).numpy()

y = 3*X+2+noise

plt.scatter(X, y)

plt.show()