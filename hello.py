import tensorflow as tf

with tf.compat.v1.Session() as sess:
  h = tf.constant("Hello")
  w = tf.constant("World!")
  hw = h + w
  ans = sess.run(hw)
  print(ans)

