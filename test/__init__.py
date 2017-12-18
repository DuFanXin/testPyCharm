import numpy as np
import tensorflow as tf
a = np.array([[1], [2]])
print(a)
W = tf.Variable(tf.zeros([4, 10]))
#with tf.Session() as s:
#    print(s.run(W))
