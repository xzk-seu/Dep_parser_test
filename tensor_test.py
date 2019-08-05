import tensorflow as tf

a = tf.random.normal((100, 100))
b = tf.random.normal((100, 500))
c = tf.matmul(a, b)
sess = tf.compat.v1.InteractiveSession()
sess.run(c)
