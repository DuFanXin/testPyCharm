import numpy as np
import tensorflow as tf
a = np.array([[1], [2]])
print(a)
#W = tf.Variable(tf.zeros([4, 10]))
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as s:
	writer = tf.summary.FileWriter('./graph', s.graph)
	print(s.run(x))
	writer.close()
