import tensorflow as tf

# 0D Tensor
d0 = tf.ones((1,))

# 1D Tensor
d1 = tf.ones((2,))

# 2D Tensor
d2 = tf.ones((2, 2))

# 3D Tensor
d3 = tf.ones((2, 2, 2))

# Print the 3D Tensor
print(d3.numpy())


# Define a 2x3 constant.
a = tf.constant(3, shape=[2, 3])

# Define a 2x2 constant.
b = tf.constant([1, 2, 3, 4], shape=[2, 2])


# Define a variable
a0 = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.float32)
a1 = tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.int16)

# Define a constant
b = tf.constant(2, tf.float32)

# Compute their product
c0 = tf.multiply(a0, b)
c1 = a0*b
