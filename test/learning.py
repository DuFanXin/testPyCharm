# -*- coding:utf-8 -*-
'''  
#====#====#====#====
# Project Name:     testPyCharm 
# File Name:        learning 
# Date:             2017/12/18 15:28 
# Using IDE:        PyCharm  
# From HomePage:    https://github.com/DuFanXin/testPyCharm
# Author:           DuFanXin 
# BlogPage:         http://blog.csdn.net/qq_30239975  
# E-mail:           18672969179@163.com
# Copyright (c) 2017, All Rights Reserved.
#====#====#====#==== 
'''

import numpy as np
import tensorflow as tf
a = np.array([[1], [2]])
print(a)
#W = tf.Variable(tf.zeros([4, 10]))
a = tf.constant([2, 2], name='a')
b = tf.constant([[0, 1], [2, 3]], name='b')
c = tf.zeros([2, 3], dtype=tf.int32, name='z')
x = tf.add(a, b, name='x')
y = tf.multiply(a, b, name='y')
with tf.Session() as s:
	#writer = tf.summary.FileWriter('./graph', s.graph)
	x, y = s.run([x, y])
	print(s.run(c))
	#writer.close()